"""
Agent service for managing AI agent interactions using Strands SDK.
"""
from strands import Agent
import logging
from backend.config import settings
from backend.tools.news_tools import (
    search_news,
    categorize_article,
    summarize_article,
    get_trending_topics
)

logger = logging.getLogger(__name__)


class AgentService:
    """Service for managing AI agent interactions."""

    def __init__(self):
        """Initialize the agent with Strands SDK."""
        self.agent = Agent(
            name="tech-news-agent",
            model=settings.CLAUDE_MODEL_ID,
            system_prompt="""You are a Tech News Aggregator AI assistant. Your purpose is to help users
            stay up-to-date with the latest technology news and developments.

            You can:
            - Search for recent news articles on specific tech topics (AI, Cloud, DevOps, Web Dev, etc.)
            - Categorize articles by technology domain
            - Summarize article content
            - Show trending tech topics

            Be informative, concise, and help users discover relevant tech news based on their interests.
            When users ask about a topic, always use the search_news tool to find recent articles.""",
            tools=[search_news, categorize_article, summarize_article, get_trending_topics]
        )
        logger.info(f"Initialized tech news agent with model: {settings.CLAUDE_MODEL_ID}")

    async def chat(self, message: str) -> str:
        """
        Send a message to the agent and get a response.

        Args:
            message: User message

        Returns:
            Agent response text
        """
        try:
            logger.info(f"Processing message: {message}")
            response = await self.agent.invoke_async(message)
            # Get the response dict and extract text from message
            result_dict = response.to_dict()

            # Extract text from the assistant's message content
            if 'message' in result_dict and 'content' in result_dict['message']:
                content = result_dict['message']['content']
                if isinstance(content, list):
                    text_parts = [block.get('text', '') for block in content if 'text' in block]
                    return ' '.join(text_parts)
                return content

            # Fallback: return the entire dict as JSON string
            return str(result_dict)
        except Exception as e:
            logger.error(f"Error in agent chat: {str(e)}")
            raise

    async def stream_chat(self, message: str):
        """
        Stream agent response chunks.

        Args:
            message: User message

        Yields:
            Response chunks as they're generated
        """
        try:
            logger.info(f"Streaming message: {message}")
            async for chunk in self.agent.stream_async(message):
                if hasattr(chunk, 'content') and chunk.content:
                    yield f"data: {chunk.content}\n\n"
        except Exception as e:
            logger.error(f"Error in agent streaming: {str(e)}")
            yield f"data: Error: {str(e)}\n\n"
