"""
Unit tests for agent service module.
"""
import pytest
from unittest.mock import Mock, AsyncMock, patch
from backend.services.agent_service import AgentService, get_weather, calculate


# Test tool functions
def test_get_weather_tool():
    """Test get_weather tool function."""
    result = get_weather("New York")

    assert "New York" in result
    assert "sunny" in result or "weather" in result.lower()


def test_calculate_tool_valid():
    """Test calculate tool with valid expression."""
    result = calculate("2 + 2")

    assert "4" in result


def test_calculate_tool_complex():
    """Test calculate tool with complex expression."""
    result = calculate("(10 + 5) * 2")

    assert "30" in result


def test_calculate_tool_invalid():
    """Test calculate tool with invalid expression."""
    result = calculate("invalid expression")

    assert "Error" in result


# Test AgentService class
@pytest.mark.asyncio
async def test_agent_service_initialization():
    """Test that AgentService initializes correctly."""
    with patch('backend.services.agent_service.Agent') as MockAgent:
        mock_agent_instance = Mock()
        MockAgent.return_value = mock_agent_instance

        service = AgentService()

        MockAgent.assert_called_once()
        call_kwargs = MockAgent.call_args.kwargs
        assert call_kwargs['name'] == "lab-assistant"
        assert 'model' in call_kwargs
        assert 'instructions' in call_kwargs
        assert 'tools' in call_kwargs
        assert len(call_kwargs['tools']) >= 2  # get_weather and calculate


@pytest.mark.asyncio
async def test_agent_service_chat():
    """Test chat method returns response."""
    with patch('backend.services.agent_service.Agent') as MockAgent:
        mock_agent_instance = Mock()
        mock_response = Mock()
        mock_response.content = "Hello! I'm ready to help."
        mock_agent_instance.run_async = AsyncMock(return_value=mock_response)
        MockAgent.return_value = mock_agent_instance

        service = AgentService()
        response = await service.chat("Hello")

        assert response == "Hello! I'm ready to help."
        mock_agent_instance.run_async.assert_called_once_with("Hello")


@pytest.mark.asyncio
async def test_agent_service_chat_error_handling():
    """Test that chat method handles errors properly."""
    with patch('backend.services.agent_service.Agent') as MockAgent:
        mock_agent_instance = Mock()
        mock_agent_instance.run_async = AsyncMock(side_effect=Exception("Test error"))
        MockAgent.return_value = mock_agent_instance

        service = AgentService()

        with pytest.raises(Exception) as exc_info:
            await service.chat("Hello")

        assert "Test error" in str(exc_info.value)


@pytest.mark.asyncio
async def test_agent_service_stream_chat():
    """Test stream_chat method yields chunks."""
    with patch('backend.services.agent_service.Agent') as MockAgent:
        mock_agent_instance = Mock()

        # Create async generator for streaming
        async def mock_stream(message):
            chunks = [
                Mock(content="Hello "),
                Mock(content="World"),
                Mock(content="!")
            ]
            for chunk in chunks:
                yield chunk

        mock_agent_instance.stream_async = mock_stream
        MockAgent.return_value = mock_agent_instance

        service = AgentService()
        chunks = []

        async for chunk in service.stream_chat("Hello"):
            chunks.append(chunk)

        assert len(chunks) == 3
        assert all("data:" in chunk for chunk in chunks)
        assert "Hello " in chunks[0]
        assert "World" in chunks[1]


@pytest.mark.asyncio
async def test_agent_service_stream_chat_error():
    """Test stream_chat error handling."""
    with patch('backend.services.agent_service.Agent') as MockAgent:
        mock_agent_instance = Mock()

        async def mock_stream_error(message):
            raise Exception("Stream error")
            yield  # This won't be reached but needed for generator

        mock_agent_instance.stream_async = mock_stream_error
        MockAgent.return_value = mock_agent_instance

        service = AgentService()
        chunks = []

        async for chunk in service.stream_chat("Hello"):
            chunks.append(chunk)

        assert len(chunks) == 1
        assert "Error" in chunks[0]


@pytest.mark.asyncio
async def test_agent_service_stream_chat_empty_content():
    """Test stream_chat with chunks that have no content."""
    with patch('backend.services.agent_service.Agent') as MockAgent:
        mock_agent_instance = Mock()

        async def mock_stream(message):
            chunks = [
                Mock(content="Valid"),
                Mock(content=""),  # Empty content
                Mock(content=None),  # None content
                Mock(spec=[]),  # No content attribute
            ]
            for chunk in chunks:
                yield chunk

        mock_agent_instance.stream_async = mock_stream
        MockAgent.return_value = mock_agent_instance

        service = AgentService()
        chunks = []

        async for chunk in service.stream_chat("Hello"):
            chunks.append(chunk)

        # Should only yield chunks with valid content
        assert len(chunks) == 1
        assert "Valid" in chunks[0]
