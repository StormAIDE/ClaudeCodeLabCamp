"""
Robotics news API endpoints.
"""
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import logging
from backend.database.db import db
from backend.tools.robotics_tools import ROBOTICS_SUBTOPICS, fetch_robotics_articles

logger = logging.getLogger(__name__)
router = APIRouter()

_VALID_SUBTOPICS: frozenset = frozenset(ROBOTICS_SUBTOPICS)


class RoboticsArticle(BaseModel):
    id: int
    title: str
    url: str
    summary: Optional[str] = None
    topic: str
    subtopic: str
    published_date: Optional[str] = None
    fetched_at: Optional[str] = None


@router.get("/robotics", response_model=List[RoboticsArticle])
async def get_robotics_news(
    subtopic: Optional[str] = Query(None, description="Robotics sub-topic filter (omit for all)"),
    limit: int = Query(20, ge=1, le=50, description="Max articles to return"),
):
    """Return robotics articles. Omit subtopic to get all, or filter by a specific sub-topic."""
    if subtopic is not None and subtopic not in _VALID_SUBTOPICS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid subtopic. Must be one of: {', '.join(sorted(_VALID_SUBTOPICS))}",
        )
    try:
        articles = db.get_robotics_articles(subtopic=subtopic, limit=limit)

        if not articles:
            fetch_subtopic = subtopic or "general"
            logger.info("No cached articles for subtopic '%s', fetching from RSS...", fetch_subtopic)
            fetched = await asyncio.to_thread(fetch_robotics_articles, fetch_subtopic, 7)
            for article in fetched:
                try:
                    db.add_robotics_article(
                        title=article["title"],
                        url=article["url"],
                        summary=article["summary"],
                        subtopic=fetch_subtopic,
                        published_date=article["published_date"],
                    )
                except Exception:
                    pass
            articles = db.get_robotics_articles(subtopic=subtopic, limit=limit)

        return articles
    except Exception as e:
        logger.error("Error fetching robotics articles: %s", str(e))
        raise HTTPException(status_code=500, detail="Failed to fetch robotics articles")


@router.get("/robotics/subtopics", response_model=List[str])
async def get_robotics_subtopics():
    """Return the list of valid robotics sub-topics."""
    return ROBOTICS_SUBTOPICS
