"""
FastAPI dependency injection for shared services.
"""
from functools import lru_cache
from backend.services.agent_service import AgentService


@lru_cache()
def get_agent_service() -> AgentService:
    """
    Get singleton instance of AgentService.

    Uses lru_cache to ensure only one instance is created
    and reused across all requests.

    Returns:
        Singleton AgentService instance
    """
    return AgentService()
