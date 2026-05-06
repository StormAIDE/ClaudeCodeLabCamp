"""
Pytest configuration and fixtures for backend tests.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.config import Settings
from backend.api.dependencies import get_agent_service


@pytest.fixture(autouse=True)
def clear_dependency_cache():
    """Clear the lru_cache for get_agent_service before each test."""
    get_agent_service.cache_clear()
    yield
    get_agent_service.cache_clear()


@pytest.fixture
def test_client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def mock_settings():
    """Create mock settings for testing."""
    return Settings(
        APP_NAME="Test App",
        APP_ENV="test",
        DEBUG=True,
        API_HOST="localhost",
        API_PORT=8000,
        CORS_ORIGINS="http://localhost:5173,http://localhost:3000",
        ANTHROPIC_API_KEY="sk-ant-test",
        CLAUDE_MODEL_ID="test-model-id"
    )


@pytest.fixture
def mock_agent_response():
    """Mock agent response object."""
    class MockResponse:
        def __init__(self, content="Test response"):
            self.content = content

    return MockResponse()


@pytest.fixture
def mock_stream_chunk():
    """Mock streaming chunk object."""
    class MockChunk:
        def __init__(self, content="chunk"):
            self.content = content

    return MockChunk
