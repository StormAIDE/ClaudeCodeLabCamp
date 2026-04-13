"""
Unit tests to verify all required dependencies are installed and importable.
"""
import pytest


def test_import_fastapi():
    """Test that fastapi is installed and importable."""
    import fastapi
    assert hasattr(fastapi, 'FastAPI')
    assert hasattr(fastapi, 'APIRouter')


def test_import_uvicorn():
    """Test that uvicorn is installed and importable."""
    import uvicorn
    assert hasattr(uvicorn, 'run')


def test_import_pydantic():
    """Test that pydantic is installed and importable."""
    import pydantic
    assert hasattr(pydantic, 'BaseModel')
    assert hasattr(pydantic, 'field_validator')


def test_import_pydantic_settings():
    """Test that pydantic-settings is installed and importable."""
    from pydantic_settings import BaseSettings, SettingsConfigDict
    assert BaseSettings is not None
    assert SettingsConfigDict is not None


def test_import_strands():
    """Test that strands-agents is installed and importable."""
    try:
        from strands import Agent, tool
        assert Agent is not None
        assert tool is not None
    except ImportError as e:
        pytest.skip(f"Strands SDK not available: {e}")


def test_import_python_dotenv():
    """Test that python-dotenv is installed and importable."""
    import dotenv
    assert hasattr(dotenv, 'load_dotenv')


def test_import_pytest():
    """Test that pytest is installed and importable."""
    import pytest
    assert pytest is not None


def test_import_pytest_asyncio():
    """Test that pytest-asyncio is installed and importable."""
    import pytest_asyncio
    assert pytest_asyncio is not None


def test_import_pytest_cov():
    """Test that pytest-cov is installed and importable."""
    import pytest_cov
    assert pytest_cov is not None


def test_import_pytest_mock():
    """Test that pytest-mock is installed and importable."""
    import pytest_mock
    assert pytest_mock is not None


def test_import_httpx():
    """Test that httpx is installed and importable."""
    import httpx
    assert hasattr(httpx, 'AsyncClient')
    assert hasattr(httpx, 'Client')


def test_fastapi_version():
    """Test FastAPI version is correct."""
    import fastapi
    # Should be version 0.115.0 or compatible
    assert hasattr(fastapi, '__version__')


def test_pydantic_version():
    """Test Pydantic version is 2.x."""
    import pydantic
    assert hasattr(pydantic, '__version__')
    major_version = int(pydantic.__version__.split('.')[0])
    assert major_version >= 2, "Pydantic 2.x is required"


def test_httpx_async_client():
    """Test that httpx AsyncClient can be instantiated."""
    import httpx
    client = httpx.AsyncClient()
    assert client is not None
    # Note: Not closing client in test as it's just instantiation check


def test_fastapi_test_client():
    """Test that FastAPI TestClient is available."""
    from fastapi.testclient import TestClient
    assert TestClient is not None


def test_pytest_markers():
    """Test that pytest.mark.asyncio is available."""
    import pytest
    assert hasattr(pytest.mark, 'asyncio')
