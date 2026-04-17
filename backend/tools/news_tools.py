"""
News aggregation tools for the tech news agent.
"""
from strands import tool
from datetime import datetime, timedelta
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


@tool
def search_news(topic: str, days: int = 7) -> str:
    """
    Search for recent tech news articles on a specific topic.

    Args:
        topic: The technology topic to search for (e.g., "AI", "Cloud", "DevOps")
        days: Number of days to look back (default: 7)

    Returns:
        A formatted string with recent news articles
    """
    try:
        # For demo purposes, return mock data
        # In production, this would call News API or RSS feeds
        articles = [
            {
                "title": f"Major breakthrough in {topic} technology announced",
                "url": f"https://example.com/article-1",
                "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "summary": f"Researchers unveil new developments in {topic} that could revolutionize the industry."
            },
            {
                "title": f"{topic} adoption grows 50% year-over-year",
                "url": f"https://example.com/article-2",
                "date": (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"),
                "summary": f"Industry report shows significant increase in {topic} adoption across enterprises."
            },
            {
                "title": f"Top 10 {topic} tools developers should know in 2025",
                "url": f"https://example.com/article-3",
                "date": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"),
                "summary": f"A comprehensive guide to the latest {topic} tools and frameworks."
            }
        ]

        result = f"Found {len(articles)} articles about {topic} from the last {days} days:\\n\\n"
        for i, article in enumerate(articles, 1):
            result += f"{i}. **{article['title']}**\\n"
            result += f"   Date: {article['date']}\\n"
            result += f"   Summary: {article['summary']}\\n"
            result += f"   URL: {article['url']}\\n\\n"

        return result
    except Exception as e:
        logger.error(f"Error searching news: {str(e)}")
        return f"Error searching for news: {str(e)}"


@tool
def categorize_article(text: str) -> str:
    """
    Categorize an article based on its content.

    Args:
        text: The article text or title to categorize

    Returns:
        The category name
    """
    # Simple keyword-based categorization
    # In production, this could use Claude's LLM for better categorization
    text_lower = text.lower()

    categories = {
        "AI/ML": ["ai", "artificial intelligence", "machine learning", "neural", "llm", "gpt"],
        "Cloud/DevOps": ["cloud", "aws", "azure", "kubernetes", "docker", "devops", "ci/cd"],
        "Web Development": ["react", "vue", "angular", "javascript", "typescript", "frontend", "backend"],
        "Mobile": ["ios", "android", "mobile", "swift", "kotlin"],
        "Security": ["security", "cybersecurity", "vulnerability", "encryption", "hack"],
        "Data Science": ["data", "analytics", "visualization", "pandas", "spark"]
    }

    for category, keywords in categories.items():
        if any(keyword in text_lower for keyword in keywords):
            return f"Category: {category}"

    return "Category: General Tech"


@tool
def summarize_article(url: str) -> str:
    """
    Fetch and summarize an article from a URL.

    Args:
        url: The URL of the article to summarize

    Returns:
        A brief summary of the article
    """
    try:
        # Mock implementation - in production, this would:
        # 1. Fetch the article content
        # 2. Extract the main text
        # 3. Use Claude to summarize
        return f"Summary: This article from {url} discusses recent developments in technology. Key points include innovation trends, industry adoption, and future predictions."
    except Exception as e:
        logger.error(f"Error summarizing article: {str(e)}")
        return f"Error summarizing article: {str(e)}"


@tool
def get_trending_topics() -> str:
    """
    Get the currently trending tech topics based on recent searches.

    Returns:
        A list of trending topics with article counts
    """
    # Mock data - in production, this would query the database
    trending = [
        {"topic": "AI", "count": 156},
        {"topic": "Cloud Computing", "count": 89},
        {"topic": "Web3", "count": 67},
        {"topic": "Cybersecurity", "count": 54},
        {"topic": "DevOps", "count": 43}
    ]

    result = "🔥 Trending Tech Topics This Week:\\n\\n"
    for i, item in enumerate(trending, 1):
        result += f"{i}. {item['topic']} - {item['count']} articles\\n"

    return result
