"""
Unit tests for agent service module.
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from anthropic import AuthenticationError, APIError


def _make_text_response(text: str) -> Mock:
    """Build a mock Anthropic Messages response with stop_reason='end_turn'."""
    block = Mock()
    block.type = "text"
    block.text = text
    response = Mock()
    response.stop_reason = "end_turn"
    response.content = [block]
    return response


def _make_tool_response(tool_name: str, tool_id: str, tool_input: dict) -> Mock:
    """Build a mock response with stop_reason='tool_use'."""
    block = Mock()
    block.type = "tool_use"
    block.name = tool_name
    block.id = tool_id
    block.input = tool_input
    response = Mock()
    response.stop_reason = "tool_use"
    response.content = [block]
    return response


@pytest.mark.asyncio
async def test_agent_service_initialization():
    """AgentService stores client and model on init."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic:
        mock_client = Mock()
        MockAnthropic.return_value = mock_client

        from backend.services.agent_service import AgentService
        service = AgentService()

        MockAnthropic.assert_called_once()
        assert service._client is mock_client


@pytest.mark.asyncio
async def test_agent_service_chat_end_turn():
    """chat() returns text when model responds with end_turn immediately."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic:
        mock_client = Mock()
        mock_client.messages.create.return_value = _make_text_response("Hello! I can help.")
        MockAnthropic.return_value = mock_client

        from backend.services.agent_service import AgentService
        service = AgentService()
        response_text, sources = await service.chat("Hello")

        assert "Hello! I can help." in response_text
        assert isinstance(sources, list)
        mock_client.messages.create.assert_called_once()


@pytest.mark.asyncio
async def test_agent_service_chat_tool_loop():
    """chat() dispatches tool call then continues to end_turn."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic, \
         patch('backend.services.agent_service.ALL_TOOL_DISPATCH') as MockDispatch:

        mock_client = Mock()
        tool_response = _make_tool_response("search_news", "tu_001", {"topic": "AI"})
        text_response = _make_text_response("Here are the AI news articles.")
        mock_client.messages.create.side_effect = [tool_response, text_response]
        MockAnthropic.return_value = mock_client

        mock_tool_fn = Mock(return_value="Found 3 articles about AI")
        MockDispatch.__getitem__ = Mock(return_value=mock_tool_fn)
        MockDispatch.get = Mock(return_value=mock_tool_fn)

        from backend.services.agent_service import AgentService
        service = AgentService()
        response_text, sources = await service.chat("Find AI news")

        assert "Here are the AI news articles." in response_text
        assert mock_client.messages.create.call_count == 2


@pytest.mark.asyncio
async def test_agent_service_chat_max_iterations():
    """chat() exits after MAX_ITERATIONS without hanging."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic, \
         patch('backend.services.agent_service.ALL_TOOL_DISPATCH') as MockDispatch:

        mock_client = Mock()
        # Always return tool_use — never end_turn
        mock_client.messages.create.return_value = _make_tool_response(
            "search_news", "tu_loop", {"topic": "test"}
        )
        MockAnthropic.return_value = mock_client

        mock_tool_fn = Mock(return_value="result")
        MockDispatch.get = Mock(return_value=mock_tool_fn)

        from backend.services.agent_service import AgentService, MAX_ITERATIONS
        service = AgentService()
        response_text, sources = await service.chat("Loop forever")

        assert "Max" in response_text or "maximum" in response_text.lower()
        assert mock_client.messages.create.call_count == MAX_ITERATIONS


@pytest.mark.asyncio
async def test_agent_service_chat_authentication_error():
    """chat() raises ValueError with clear message on authentication failure."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic:
        mock_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 401
        mock_client.messages.create.side_effect = AuthenticationError(
            message="Invalid API key",
            response=mock_response,
            body={}
        )
        MockAnthropic.return_value = mock_client

        from backend.services.agent_service import AgentService
        service = AgentService()

        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
            await service.chat("Hello")


@pytest.mark.asyncio
async def test_agent_service_chat_unknown_tool():
    """chat() handles unknown tool names gracefully without crashing."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic:
        mock_client = Mock()
        tool_response = _make_tool_response("nonexistent_tool", "tu_bad", {})
        text_response = _make_text_response("I handled it.")
        mock_client.messages.create.side_effect = [tool_response, text_response]
        MockAnthropic.return_value = mock_client

        from backend.services.agent_service import AgentService
        service = AgentService()
        response_text, _ = await service.chat("Use a bad tool")

        # Should not raise; second call produces the final text
        assert "I handled it." in response_text


@pytest.mark.asyncio
async def test_agent_service_chat_error_handling():
    """chat() propagates unexpected exceptions."""
    with patch('backend.services.agent_service.Anthropic') as MockAnthropic:
        mock_client = Mock()
        mock_client.messages.create.side_effect = RuntimeError("Unexpected")
        MockAnthropic.return_value = mock_client

        from backend.services.agent_service import AgentService
        service = AgentService()

        with pytest.raises(RuntimeError, match="Unexpected"):
            await service.chat("Hello")
