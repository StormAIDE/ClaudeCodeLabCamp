"""
Robotics news aggregation tools.
"""
from datetime import datetime, timedelta
from typing import List, Dict
import logging
import feedparser
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

ROBOTICS_SUBTOPICS: List[str] = [
    "general",
    "humanoids",
    "drones",
    "ros",
    "research",
    "industrial",
]

ROBOTICS_RSS_FEEDS: Dict[str, List[str]] = {
    "general": [
        "https://www.therobotreport.com/feed/",
        "https://roboticsandautomationnews.com/feed/",
    ],
    "humanoids": [
        "https://www.therobotreport.com/category/humanoid-robots/feed/",
    ],
    "drones": [
        "https://www.suasnews.com/feed/",
        "https://dronelife.com/feed/",
    ],
    "ros": [
        "https://discourse.ros.org/latest.rss",
    ],
    "research": [
        "https://arxiv.org/rss/cs.RO",
        "https://spectrum.ieee.org/feeds/blog/automaton.rss",
    ],
    "industrial": [
        "https://www.therobotreport.com/category/industrial-robots/feed/",
    ],
}

# Thread-safe source tracker for the current query
_current_robotics_sources: List[Dict] = []


def clear_robotics_sources():
    global _current_robotics_sources
    _current_robotics_sources = []


def get_robotics_sources() -> List[Dict]:
    return _current_robotics_sources.copy()


def add_robotics_source(article: Dict):
    global _current_robotics_sources
    _current_robotics_sources.append(article)


def fetch_robotics_articles(subtopic: str, days: int = 7) -> List[Dict]:
    """Fetch robotics articles from RSS feeds for the given subtopic."""
    cutoff_date = datetime.now() - timedelta(days=days)
    feeds = ROBOTICS_RSS_FEEDS.get(subtopic, ROBOTICS_RSS_FEEDS["general"])
    articles = []

    for feed_url in feeds:
        try:
            logger.info("Fetching robotics RSS feed: %s", feed_url)
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:5]:
                try:
                    pub_date = None
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        pub_date = datetime(*entry.published_parsed[:6])
                    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                        pub_date = datetime(*entry.updated_parsed[:6])
                    else:
                        pub_date = datetime.now()

                    if pub_date < cutoff_date:
                        continue

                    summary = entry.get('summary', '')
                    if summary:
                        soup = BeautifulSoup(summary, 'html.parser')
                        summary = soup.get_text()[:200] + "..."
                    else:
                        summary = "No summary available"

                    articles.append({
                        "title": entry.get('title', 'No title'),
                        "url": entry.get('link', ''),
                        "summary": summary,
                        "published_date": pub_date.isoformat(),
                        "subtopic": subtopic,
                    })
                except Exception as e:
                    logger.error("Error parsing robotics entry: %s", str(e))
                    continue

        except Exception as e:
            logger.error("Error fetching robotics feed %s: %s", feed_url, str(e))
            continue

    return articles


def search_robotics_news(subtopic: str = "general", days: int = 7) -> str:
    """
    Search for recent robotics news articles on a specific sub-topic.

    Args:
        subtopic: Robotics sub-topic (general, humanoids, drones, ros, research, industrial)
        days: Number of days to look back (default: 7)

    Returns:
        A formatted string with recent robotics news articles
    """
    if subtopic not in ROBOTICS_SUBTOPICS:
        logger.warning("Invalid robotics subtopic requested: %s", subtopic)
        return (
            f"Invalid subtopic '{subtopic}'. "
            f"Valid options: {', '.join(ROBOTICS_SUBTOPICS)}"
        )

    try:
        from backend.database.db import db

        cached = db.get_robotics_articles(subtopic=subtopic, limit=10)
        articles = cached[:5]

        if not articles:
            return f"No recent robotics articles found for sub-topic: {subtopic}"

        for article in articles:
            add_robotics_source(article)

        result = f"🤖 Found {len(articles)} recent robotics articles [{subtopic}]:\n\n"
        for i, article in enumerate(articles, 1):
            result += f"{i}. **{article['title']}**\n"
            result += f"   📅 {article.get('published_date', 'Unknown date')}\n"
            result += f"   📝 {article['summary']}\n"
            result += f"   🔗 Source: {article['url']}\n\n"

        return result
    except Exception as e:
        logger.error("Error searching robotics news: %s", str(e))
        return f"Error searching for robotics news: {str(e)}"


ROBOTICS_TOOL_SCHEMAS: List[Dict] = [
    {
        "name": "search_robotics_news",
        "description": (
            "Search for recent robotics news articles on a specific sub-topic. "
            "Valid subtopics: general, humanoids, drones, ros, research, industrial."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "subtopic": {
                    "type": "string",
                    "description": "Robotics sub-topic (general, humanoids, drones, ros, research, industrial)",
                    "enum": ROBOTICS_SUBTOPICS,
                },
                "days": {
                    "type": "integer",
                    "description": "Number of days to look back (default: 7)",
                }
            },
            "required": []
        }
    }
]

ROBOTICS_TOOL_DISPATCH: Dict = {
    "search_robotics_news": search_robotics_news,
}
