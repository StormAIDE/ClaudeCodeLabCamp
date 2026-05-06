"""
Agent service using AWS Bedrock with Strands SDK.
"""
import asyncio
import logging
import os
from backend.config import settings
from backend.tools.news_tools import clear_sources, get_sources
from backend.tools.robotics_tools import search_robotics_news

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

class AgentService:
    """Service for managing AI agent interactions using AWS Bedrock via Strands SDK."""

    def __init__(self):
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
            "AgentService initialized with Bedrock — model: %s, region: %s",
            settings.CLAUDE_MODEL_ID,
            settings.AWS_DEFAULT_REGION,
        )

    # ── Public interface ──────────────────────────────────────────────────────

    async def chat(self, message: str) -> tuple[str, list]:
        try:
            clear_sources()
            logger.info("Bedrock chat: %s", message[:50])
            result = await asyncio.to_thread(self._agent, message)
            return str(result).strip(), get_sources()
        except Exception as e:
            logger.error("Bedrock chat error: %s", str(e))
            raise

    async def stream_chat(self, message: str):
        try:
            logger.info("Bedrock stream: %s", message[:50])
            async for chunk in self._agent.stream_async(message):
                if isinstance(chunk, dict) and chunk.get("data"):
                    yield f"data: {chunk['data']}\n\n"
        except Exception as e:
            logger.error("Bedrock stream error: %s", str(e))
            yield f"data: Error: {str(e)}\n\n"
