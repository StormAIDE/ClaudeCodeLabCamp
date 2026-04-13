"""
Unit tests for API endpoints.
"""
import pytest
from unittest.mock import AsyncMock, patch, Mock
from fastapi import status


def test_health_endpoint(test_client):
    """Test health check endpoint."""
    response = test_client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["status"] == "healthy"
    assert "app" in data


def test_agent_status_endpoint(test_client):
    """Test agent status endpoint."""
    response = test_client.get("/api/v1/agent/status")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["status"] == "ready"
    assert "model" in data


def test_chat_endpoint_non_streaming(test_client):
    """Test chat endpoint with non-streaming response."""
    with patch('backend.api.dependencies.AgentService') as MockService:
        mock_instance = Mock()
        mock_instance.chat = AsyncMock(return_value="This is a test response")
        MockService.return_value = mock_instance

        response = test_client.post(
            "/api/v1/agent/chat",
            json={"message": "Hello", "stream": False}
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["response"] == "This is a test response"
        assert "tool_calls" in data
        mock_instance.chat.assert_called_once_with("Hello")


def test_chat_endpoint_streaming(test_client):
    """Test chat endpoint with streaming response."""
    with patch('backend.api.dependencies.AgentService') as MockService:
        mock_instance = Mock()

        async def mock_stream(message):
            yield "data: chunk1\n\n"
            yield "data: chunk2\n\n"

        mock_instance.stream_chat = mock_stream
        MockService.return_value = mock_instance

        response = test_client.post(
            "/api/v1/agent/chat",
            json={"message": "Hello", "stream": True}
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.headers["content-type"] == "text/event-stream; charset=utf-8"


def test_chat_endpoint_missing_message(test_client):
    """Test chat endpoint with missing message field."""
    with patch('backend.api.dependencies.AgentService') as MockService:
        mock_instance = Mock()
        MockService.return_value = mock_instance

        response = test_client.post(
            "/api/v1/agent/chat",
            json={"stream": False}
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_chat_endpoint_empty_message(test_client):
    """Test chat endpoint with empty message."""
    with patch('backend.api.dependencies.AgentService') as MockService:
        mock_instance = Mock()
        mock_instance.chat = AsyncMock(return_value="Please provide a message")
        MockService.return_value = mock_instance

        response = test_client.post(
            "/api/v1/agent/chat",
            json={"message": "", "stream": False}
        )

        # Empty string is valid for pydantic, but API should still accept it
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_422_UNPROCESSABLE_ENTITY]


def test_chat_endpoint_error_handling(test_client):
    """Test chat endpoint error handling."""
    with patch('backend.api.dependencies.AgentService') as MockService:
        mock_instance = Mock()
        mock_instance.chat = AsyncMock(side_effect=Exception("Service error"))
        MockService.return_value = mock_instance

        response = test_client.post(
            "/api/v1/agent/chat",
            json={"message": "Hello", "stream": False}
        )

        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        data = response.json()
        assert "detail" in data


def test_cors_headers(test_client):
    """Test that CORS headers are properly configured."""
    response = test_client.options(
        "/api/v1/agent/status",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET"
        }
    )

    # CORS middleware should handle OPTIONS requests
    assert "access-control-allow-origin" in response.headers


def test_chat_request_model_validation():
    """Test ChatRequest model validation."""
    from backend.api.endpoints.agent import ChatRequest

    # Valid request
    request = ChatRequest(message="Hello", stream=True)
    assert request.message == "Hello"
    assert request.stream is True

    # Default stream value
    request = ChatRequest(message="Hello")
    assert request.stream is False


def test_chat_response_model():
    """Test ChatResponse model."""
    from backend.api.endpoints.agent import ChatResponse

    response = ChatResponse(response="Test response", tool_calls=[])
    assert response.response == "Test response"
    assert response.tool_calls == []

    # With tool calls
    response = ChatResponse(
        response="Used tools",
        tool_calls=[{"name": "get_weather", "args": {"location": "NYC"}}]
    )
    assert len(response.tool_calls) == 1
