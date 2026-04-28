"""
Agent service — auto-selects AWS Bedrock (Strands SDK) or direct Anthropic API
depending on whether AWS credentials are present in the environment.
"""
import asyncio
import logging
from anthropic import Anthropic, AuthenticationError, APIError
from backend.config import settings
from backend.tools.news_tools import TOOL_SCHEMAS, TOOL_DISPATCH, clear_sources, get_sources
from backend.tools.robotics_tools import (
    search_robotics_news,
    ROBOTICS_TOOL_SCHEMAS,
    ROBOTICS_TOOL_DISPATCH,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a Tech News Aggregator AI assistant. Your purpose is to help users
stay up-to-date with the latest technology news and developments.

You can:
- Search for recent news articles on specific tech topics (AI, Cloud, DevOps, Web Dev, Robotics, etc.)
- Search across ALL cached news feeds for specific companies, people, or events
- Categorize articles by technology domain
- Summarize article content
- Show trending tech topics

How to choose the right tool:
- For broad topic searches (e.g. "AI news", "cloud updates"): use search_news
- For specific queries (e.g. "Boston Dynamics", "GPT-5", "AWS re:Invent"): use search_all_news
- For robotics-specific news: use search_robotics_news
- For trending topics: use get_trending_topics

The news database is continuously populated by the topic digest pages. search_all_news and
search_robotics_news read from this cache first (fast), then fetch live if needed.

Be informative, concise, and help users discover relevant tech news based on their interests.
Always use a search tool to find recent articles before answering news questions."""

ALL_TOOL_SCHEMAS = TOOL_SCHEMAS + ROBOTICS_TOOL_SCHEMAS
ALL_TOOL_DISPATCH = {**TOOL_DISPATCH, **ROBOTICS_TOOL_DISPATCH}

MAX_ITERATIONS = 10


class AgentService:
    """Service for managing AI agent interactions.

    Uses AWS Bedrock via Strands SDK when AWS credentials are configured,
    otherwise falls back to the direct Anthropic API.
    """

    def __init__(self):
        if settings.use_bedrock:
            self._init_bedrock()
        else:
            self._init_anthropic()

    # ── Provider initialisation ───────────────────────────────────────────────

    def _init_bedrock(self):
        import os
        from strands import Agent
        from strands.models.bedrock import BedrockModel
        from backend.tools import news_tools, robotics_tools

        # botocore reads credentials from os.environ, not from pydantic .env values
        if settings.AWS_ACCESS_KEY_ID:
            os.environ["AWS_ACCESS_KEY_ID"] = settings.AWS_ACCESS_KEY_ID
        if settings.AWS_SECRET_ACCESS_KEY:
            os.environ["AWS_SECRET_ACCESS_KEY"] = settings.AWS_SECRET_ACCESS_KEY
        if settings.AWS_SESSION_TOKEN:
            os.environ["AWS_SESSION_TOKEN"] = settings.AWS_SESSION_TOKEN
        os.environ["AWS_DEFAULT_REGION"] = settings.AWS_DEFAULT_REGION

        bedrock_model = BedrockModel(
            model_id=settings.CLAUDE_MODEL_ID,
            region_name=settings.AWS_DEFAULT_REGION,
        )

        self._provider = "bedrock"
        self._agent = Agent(
            model=bedrock_model,
            callback_handler=None,
            system_prompt=SYSTEM_PROMPT,
            tools=[
                news_tools.search_news,
                news_tools.search_all_news,
                news_tools.categorize_article,
                news_tools.summarize_article,
                news_tools.get_trending_topics,
                robotics_tools.search_robotics_news,
            ],
        )
        logger.info(
            "AgentService initialised — provider: bedrock, model: %s",
            settings.CLAUDE_MODEL_ID,
        )

    def _init_anthropic(self):
        self._provider = "anthropic"
        self._client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self._model = settings.CLAUDE_MODEL_ID
        logger.info(
            "AgentService initialised — provider: anthropic, model: %s, key set: %s",
            self._model,
            bool(settings.ANTHROPIC_API_KEY),
        )

    # ── Public interface ──────────────────────────────────────────────────────

    async def chat(self, message: str) -> tuple[str, list]:
        if self._provider == "bedrock":
            return await self._chat_bedrock(message)
        return await self._chat_anthropic(message)

    async def stream_chat(self, message: str):
        if self._provider == "bedrock":
            async for chunk in self._stream_bedrock(message):
                yield chunk
        else:
            async for chunk in self._stream_anthropic(message):
                yield chunk

    # ── Bedrock / Strands paths ───────────────────────────────────────────────

    async def _chat_bedrock(self, message: str) -> tuple[str, list]:
        try:
            clear_sources()
            logger.info("Bedrock chat: %s", message[:50])
            result = await asyncio.to_thread(self._agent, message)
            return str(result).strip(), get_sources()
        except Exception as e:
            logger.error("Bedrock chat error: %s", str(e))
            raise

    async def _stream_bedrock(self, message: str):
        try:
            logger.info("Bedrock stream: %s", message[:50])
            async for chunk in self._agent.stream_async(message):
                if isinstance(chunk, dict) and chunk.get("data"):
                    yield f"data: {chunk['data']}\n\n"
        except Exception as e:
            logger.error("Bedrock stream error: %s", str(e))
            yield f"data: Error: {str(e)}\n\n"

    # ── Anthropic direct API paths ────────────────────────────────────────────

    async def _chat_anthropic(self, message: str) -> tuple[str, list]:
        try:
            clear_sources()
            messages = [{"role": "user", "content": message}]

            for iteration in range(MAX_ITERATIONS):
                logger.info("Anthropic loop iteration %d", iteration + 1)

                response = await asyncio.to_thread(
                    self._client.messages.create,
                    model=self._model,
                    system=SYSTEM_PROMPT,
                    tools=ALL_TOOL_SCHEMAS,
                    messages=messages,
                    max_tokens=4096,
                )

                if response.stop_reason == "end_turn":
                    text = " ".join(
                        block.text for block in response.content if block.type == "text"
                    )
                    return text, get_sources()

                tool_blocks = [b for b in response.content if b.type == "tool_use"]
                if not tool_blocks:
                    text = " ".join(
                        block.text for block in response.content if block.type == "text"
                    )
                    return text or "No response generated.", get_sources()

                messages.append({"role": "assistant", "content": response.content})

                tool_results = []
                for block in tool_blocks:
                    tool_fn = ALL_TOOL_DISPATCH.get(block.name)
                    if tool_fn is None:
                        logger.warning("Unknown tool requested: %s", block.name)
                        result = f"Error: unknown tool '{block.name}'"
                    else:
                        try:
                            result = str(tool_fn(**block.input))
                        except Exception as e:
                            logger.error("Tool %s raised: %s", block.name, str(e))
                            result = f"Error executing {block.name}: {str(e)}"

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

                messages.append({"role": "user", "content": tool_results})

            logger.warning("Anthropic agent reached max iterations")
            return "I reached the maximum number of steps. Please try a more specific query.", get_sources()

        except AuthenticationError as e:
            logger.error("Anthropic authentication failed: %s", str(e))
            raise ValueError("Invalid ANTHROPIC_API_KEY. Check your .env file.") from e
        except APIError as e:
            logger.error("Anthropic API error: %s", str(e))
            raise
        except Exception as e:
            logger.error("Anthropic chat error: %s", str(e))
            raise

    async def _stream_anthropic(self, message: str):
        queue: asyncio.Queue = asyncio.Queue()
        _SENTINEL = object()
        loop = asyncio.get_event_loop()

        def _producer():
            try:
                with self._client.messages.stream(
                    model=self._model,
                    system=SYSTEM_PROMPT,
                    tools=ALL_TOOL_SCHEMAS,
                    messages=[{"role": "user", "content": message}],
                    max_tokens=4096,
                ) as stream:
                    for text in stream.text_stream:
                        loop.call_soon_threadsafe(queue.put_nowait, text)
            except AuthenticationError as e:
                loop.call_soon_threadsafe(queue.put_nowait, f"__ERROR__:Invalid API key: {str(e)}")
            except APIError as e:
                loop.call_soon_threadsafe(queue.put_nowait, f"__ERROR__:{str(e)}")
            except Exception as e:
                loop.call_soon_threadsafe(queue.put_nowait, f"__ERROR__:{str(e)}")
            finally:
                loop.call_soon_threadsafe(queue.put_nowait, _SENTINEL)

        loop.run_in_executor(None, _producer)

        while True:
            item = await queue.get()
            if item is _SENTINEL:
                break
            if isinstance(item, str) and item.startswith("__ERROR__:"):
                logger.error("Anthropic stream error: %s", item[10:])
                yield f"data: Error: {item[10:]}\n\n"
                break
            yield f"data: {item}\n\n"
