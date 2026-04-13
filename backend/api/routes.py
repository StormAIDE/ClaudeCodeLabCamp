"""
API route handlers.
"""
from fastapi import APIRouter
from backend.api.endpoints import agent

router = APIRouter()

# Include endpoint modules
router.include_router(agent.router, prefix="/agent", tags=["agent"])
