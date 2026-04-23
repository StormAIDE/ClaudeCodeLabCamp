"""
News aggregation tools for the tech news agent.
"""
try:
    from strands import tool as _strands_tool
except ImportError:
    def _strands_tool(fn):  # no-op when strands not installed
        return fn

from datetime import datetime, timedelta
from typing import List, Dict
import logging
import feedparser
import requests
from bs4 import BeautifulSoup
from backend.database.db import db

logger = logging.getLogger(__name__)

# Thread-safe storage for sources used in current query
_current_sources: List[Dict] = []


def clear_sources():
    """Clear the sources list for a new query."""
    global _current_sources
    _current_sources = []


def get_sources() -> List[Dict]:
    """Get the list of sources used in the current query."""
    return _current_sources.copy()


def add_source(article: Dict):
    """Add an article to the sources list."""
    global _current_sources
    _current_sources.append(article)

# RSS feeds for different tech news sources
RSS_FEEDS = {
    "general": [
        "https://techcrunch.com/feed/",
        "https://www.theverge.com/rss/index.xml",
        "https://news.ycombinator.com/rss",
    ],
    "ai": [
        "https://techcrunch.com/category/artificial-intelligence/feed/",
    ],
    "cloud": [
        "https://aws.amazon.com/blogs/aws/feed/",
    ],
    "security": [
        "https://feeds.feedburner.com/TheHackersNews",
    ]
}


def fetch_rss_articles(topic: str, days: int = 7) -> List[Dict]:
    """Fetch articles from RSS feeds and cache in database."""
    cutoff_date = datetime.now() - timedelta(days=days)
    articles = []

    # Determine which feeds to use based on topic
    topic_lower = topic.lower()
    feeds = RSS_FEEDS["general"].copy()

    if "ai" in topic_lower or "ml" in topic_lower:
        feeds.extend(RSS_FEEDS["ai"])
    elif "cloud" in topic_lower or "devops" in topic_lower:
        feeds.extend(RSS_FEEDS["cloud"])
    elif "security" in topic_lower:
        feeds.extend(RSS_FEEDS["security"])

    for feed_url in feeds:
        try:
            logger.info(f"Fetching RSS feed: {feed_url}")
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:5]:  # Limit to 5 articles per feed
                try:
                    # Parse published date
                    pub_date = None
                    if hasattr(entry, 'published_parsed'):
                        pub_date = datetime(*entry.published_parsed[:6])
                    elif hasattr(entry, 'updated_parsed'):
                        pub_date = datetime(*entry.updated_parsed[:6])
                    else:
                        pub_date = datetime.now()

                    # Skip if too old
                    if pub_date < cutoff_date:
                        continue

                    # Extract summary
                    summary = entry.get('summary', '')
                    if summary:
                        soup = BeautifulSoup(summary, 'html.parser')
                        summary = soup.get_text()[:200] + "..."
                    else:
                        summary = "No summary available"

                    article = {
                        "title": entry.get('title', 'No title'),
                        "url": entry.get('link', ''),
                        "summary": summary,
                        "published_date": pub_date.isoformat(),
                    }

                    articles.append(article)
                except Exception as e:
                    logger.error(f"Error parsing entry: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Error fetching feed {feed_url}: {str(e)}")
            continue

    return articles


@_strands_tool
def search_news(topic: str, days: int = 7) -> str:
    """
    Search for recent tech news articles on a specific topic.
    First checks database cache, then fetches from RSS feeds if needed.

    Args:
        topic: The technology topic to search for (e.g., "AI", "Cloud", "DevOps")
        days: Number of days to look back (default: 7)

    Returns:
        A formatted string with recent news articles and their sources
    """
    try:
        # First, check database for cached articles
        cached_articles = db.get_articles_by_topic(topic, limit=10)

        # If we have recent cached articles, use them
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_cached = [
            a for a in cached_articles
            if datetime.fromisoformat(a['fetched_at']) > cutoff_date
        ]

        if len(recent_cached) >= 3:
            logger.info(f"Using {len(recent_cached)} cached articles for topic: {topic}")
            articles = recent_cached[:5]
        else:
            # Fetch fresh articles from RSS feeds
            logger.info(f"Fetching fresh articles for topic: {topic}")
            fetched = fetch_rss_articles(topic, days)

            # Categorize and save to database
            for article in fetched:
                category = categorize_article(article['title'] + " " + article['summary'])
                category_name = category.replace("Category: ", "")

                try:
                    db.add_article(
                        title=article['title'],
                        url=article['url'],
                        summary=article['summary'],
                        topic=category_name,
                        published_date=article['published_date']
                    )
                except Exception as e:
                    logger.error(f"Error saving article: {str(e)}")

            articles = fetched[:5]

        if not articles:
            return f"No recent articles found for topic: {topic}"

        # Add articles to sources list for frontend display
        for article in articles:
            add_source(article)

        # Format response with sources
        result = f"📰 Found {len(articles)} recent articles about {topic}:\n\n"
        for i, article in enumerate(articles, 1):
            result += f"{i}. **{article['title']}**\n"
            result += f"   📅 {article.get('published_date', 'Unknown date')}\n"
            result += f"   📝 {article['summary']}\n"
            result += f"   🔗 Source: {article['url']}\n\n"

        return result
    except Exception as e:
        logger.error(f"Error searching news: {str(e)}")
        return f"Error searching for news: {str(e)}"


@_strands_tool
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


@_strands_tool
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


@_strands_tool
def get_trending_topics() -> str:
    """
    Get the currently trending tech topics based on articles in database.

    Returns:
        A list of trending topics with article counts
    """
    try:
        trending = db.get_trending_topics(days=7, limit=10)

        if not trending:
            return "No trending topics found. Try searching for specific topics first!"

        result = "🔥 Trending Tech Topics This Week:\n\n"
        for i, item in enumerate(trending, 1):
            result += f"{i}. {item['topic']} - {item['count']} articles\n"

        return result
    except Exception as e:
        logger.error(f"Error getting trending topics: {str(e)}")
        return f"Error getting trending topics: {str(e)}"


@_strands_tool
def search_all_news(query: str, days: int = 7) -> str:
    """
    Search for news across all cached articles from all topic feeds.

    Searches the local database first for speed, falls back to live RSS fetch
    if nothing found. Use this for specific queries like company names, people,
    or events.

    Args:
        query: The search query (e.g., "Boston Dynamics", "GPT-5", "AWS re:Invent")
        days: Number of days to look back (default: 7)

    Returns:
        A formatted string with matching news articles and their sources
    """
    try:
        articles = db.search_articles(query, days, limit=8)

        if not articles:
            # Fall back to live RSS fetch
            logger.info("No DB results for '%s'; falling back to RSS fetch", query)
            fetched = fetch_rss_articles(query, days)

            for article in fetched:
                category = categorize_article(article['title'] + " " + article['summary'])
                category_name = category.replace("Category: ", "")
                try:
                    db.add_article(
                        title=article['title'],
                        url=article['url'],
                        summary=article['summary'],
                        topic=category_name,
                        published_date=article['published_date'],
                    )
                except Exception as e:
                    logger.error("Error saving article during search_all_news fallback: %s", str(e))

            articles = fetched[:8]

        if not articles:
            return f"No recent articles found matching: {query}"

        for article in articles:
            add_source(article)

        result = f"Found {len(articles)} articles matching '{query}':\n\n"
        for i, article in enumerate(articles, 1):
            result += f"{i}. **{article['title']}**\n"
            result += f"   {article.get('published_date', 'Unknown date')}\n"
            result += f"   {article['summary']}\n"
            result += f"   Source: {article['url']}\n\n"

        return result
    except Exception as e:
        logger.error("Error in search_all_news: %s", str(e))
        return f"Error searching news: {str(e)}"


# Anthropic tool schemas — consumed by agent_service agentic loop
TOOL_SCHEMAS = [
    {
        "name": "search_news",
        "description": (
            "Search for recent tech news articles on a specific topic. "
            "First checks database cache, then fetches from RSS feeds if needed."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The technology topic to search for (e.g., 'AI', 'Cloud', 'DevOps')"
                },
                "days": {
                    "type": "integer",
                    "description": "Number of days to look back (default: 7)"
                }
            },
            "required": ["topic"]
        }
    },
    {
        "name": "categorize_article",
        "description": "Categorize an article based on its content using keyword matching.",
        "input_schema": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The article text or title to categorize"
                }
            },
            "required": ["text"]
        }
    },
    {
        "name": "summarize_article",
        "description": "Fetch and summarize an article from a URL.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the article to summarize"
                }
            },
            "required": ["url"]
        }
    },
    {
        "name": "get_trending_topics",
        "description": "Get the currently trending tech topics based on articles in the database.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "search_all_news",
        "description": (
            "Search for news across all cached articles from all topic feeds "
            "(robotics, AI, cloud, etc.). Searches the local database first for speed, "
            "falls back to live RSS fetch if nothing found. Use this for specific queries "
            "like company names, people, or events."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query (e.g., 'Boston Dynamics', 'GPT-5', 'AWS re:Invent')"
                },
                "days": {
                    "type": "integer",
                    "description": "Number of days to look back (default: 7)"
                }
            },
            "required": ["query"]
        }
    },
]

# Maps tool names to callable Python functions
TOOL_DISPATCH: Dict = {
    "search_news": search_news,
    "categorize_article": categorize_article,
    "summarize_article": summarize_article,
    "get_trending_topics": get_trending_topics,
    "search_all_news": search_all_news,
}
