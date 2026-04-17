"""
API route handlers.
"""
from fastapi import APIRouter
from backend.api.endpoints import agent, news

router = APIRouter()

# Include endpoint modules
router.include_router(agent.router, prefix="/agent", tags=["agent"])
router.include_router(news.router, tags=["news"])
