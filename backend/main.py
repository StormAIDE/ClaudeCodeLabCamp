"""
FastAPI application entry point.
"""
import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.api.routes import router

logger = logging.getLogger(__name__)

SCRAPE_INTERVAL_SECONDS = 120  # 2 minutes


async def _scrape_all_feeds():
    """Scrape all RSS feeds and persist articles to the DB."""
    from backend.tools.news_tools import fetch_rss_articles, categorize_article, RSS_FEEDS
    from backend.tools.robotics_tools import fetch_robotics_articles, ROBOTICS_RSS_FEEDS, ROBOTICS_SUBTOPICS
    from backend.database.db import db

    # General / tech feeds
    for topic in RSS_FEEDS:
        try:
            articles = await asyncio.to_thread(fetch_rss_articles, topic)
            for article in articles:
                category = categorize_article(article["title"] + " " + article["summary"])
                try:
                    db.add_article(
                        title=article["title"],
                        url=article["url"],
                        summary=article["summary"],
                        topic=category.replace("Category: ", ""),
                        published_date=article["published_date"],
                    )
                except Exception:
                    pass
        except Exception as e:
            logger.error("Scraper error (topic=%s): %s", topic, e)

    # Robotics feeds
    for subtopic in ROBOTICS_SUBTOPICS:
        try:
            articles = await asyncio.to_thread(fetch_robotics_articles, subtopic)
            for article in articles:
                try:
                    db.add_robotics_article(
                        title=article["title"],
                        url=article["url"],
                        summary=article["summary"],
                        subtopic=subtopic,
                        published_date=article["published_date"],
                    )
                except Exception:
                    pass
        except Exception as e:
            logger.error("Scraper error (subtopic=%s): %s", subtopic, e)

    logger.info("Background scrape complete.")


async def _scraper_loop():
    while True:
        try:
            logger.info("Background scraper: starting run...")
            await _scrape_all_feeds()
        except Exception as e:
            logger.error("Background scraper failed: %s", e)
        await asyncio.sleep(SCRAPE_INTERVAL_SECONDS)


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(_scraper_loop())
    yield
    task.cancel()


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "app": settings.APP_NAME}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
