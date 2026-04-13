"""
Agent endpoints for AI interactions.
"""
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, field_validator
from backend.services.agent_service import AgentService
from backend.api.dependencies import get_agent_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str
    stream: bool = False

    @field_validator('message')
    @classmethod
    def validate_message_not_empty(cls, v: str) -> str:
        """Validate that message is not empty or whitespace."""
        if not v or not v.strip():
            raise ValueError("Message cannot be empty or whitespace")
        return v.strip()


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    response: str
    tool_calls: list = []


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    agent_service: AgentService = Depends(get_agent_service)
):
    """
    Chat with the AI agent.
    Supports both streaming and non-streaming responses.
    """
    try:

        if request.stream:
            async def generate():
                async for chunk in agent_service.stream_chat(request.message):
                    yield chunk

            return StreamingResponse(generate(), media_type="text/event-stream")
        else:
            response = await agent_service.chat(request.message)
            return ChatResponse(response=response, tool_calls=[])

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
async def agent_status():
    """Check agent service status."""
    return {"status": "ready", "model": "claude-4-bedrock"}
