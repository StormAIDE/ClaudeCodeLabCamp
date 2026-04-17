"""
News API endpoints.
"""
from fastapi import APIRouter, Query, HTTPException
from typing import List, Dict
from backend.database.db import db
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/news")
async def get_news(
    topic: str = Query(None, description="Filter by topic"),
    days: int = Query(7, description="Number of days to look back", ge=1, le=30)
) -> List[Dict]:
    """
    Get news articles, optionally filtered by topic.

    Args:
        topic: Optional topic filter (e.g., "AI", "Cloud")
        days: Number of days to look back (1-30)

    Returns:
        List of articles
    """
    try:
        if topic:
            articles = db.get_articles_by_topic(topic, limit=20)
        else:
            # Get all recent articles
            articles = db.get_articles_by_topic("", limit=20)

        logger.info(f"Retrieved {len(articles)} articles for topic: {topic or 'all'}")
        return articles
    except Exception as e:
        logger.error(f"Error fetching news: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch news articles")


@router.get("/trending")
async def get_trending(
    days: int = Query(7, description="Number of days to analyze", ge=1, le=30),
    limit: int = Query(5, description="Number of trending topics", ge=1, le=20)
) -> List[Dict]:
    """
    Get trending tech topics.

    Args:
        days: Number of days to analyze (1-30)
        limit: Number of topics to return (1-20)

    Returns:
        List of trending topics with article counts
    """
    try:
        trending = db.get_trending_topics(days=days, limit=limit)
        logger.info(f"Retrieved {len(trending)} trending topics")
        return trending
    except Exception as e:
        logger.error(f"Error fetching trending topics: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch trending topics")
