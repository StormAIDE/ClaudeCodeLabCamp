"""
Unit tests for configuration module.
"""
import pytest
from backend.config import Settings


def test_settings_default_values():
    """Test that settings have correct default values."""
    settings = Settings()

    assert settings.APP_NAME == "ClaudeCode Lab Agent"
    assert settings.APP_ENV == "development"
    assert settings.DEBUG is True
    assert settings.API_HOST == "0.0.0.0"
    assert settings.API_PORT == 8000
    assert isinstance(settings.CORS_ORIGINS, list)
    assert len(settings.CORS_ORIGINS) >= 2


def test_settings_cors_origins_parsing():
    """Test that CORS_ORIGINS is correctly parsed from string."""
    settings = Settings(CORS_ORIGINS="http://test1.com,http://test2.com")

    assert isinstance(settings.CORS_ORIGINS, list)
    assert len(settings.CORS_ORIGINS) == 2
    assert "http://test1.com" in settings.CORS_ORIGINS
    assert "http://test2.com" in settings.CORS_ORIGINS


def test_settings_cors_origins_with_spaces():
    """Test CORS_ORIGINS parsing with spaces."""
    settings = Settings(CORS_ORIGINS="http://test1.com, http://test2.com, http://test3.com")

    assert len(settings.CORS_ORIGINS) == 3
    assert all("http://" in origin for origin in settings.CORS_ORIGINS)


def test_settings_cors_origins_list():
    """Test that CORS_ORIGINS accepts a list directly."""
    origins = ["http://test1.com", "http://test2.com"]
    settings = Settings(CORS_ORIGINS=origins)

    assert settings.CORS_ORIGINS == origins


def test_settings_custom_values():
    """Test settings with custom values."""
    settings = Settings(
        APP_NAME="Custom App",
        API_PORT=9000,
        DEBUG=False,
        CLAUDE_MODEL_ID="custom-model-id"
    )

    assert settings.APP_NAME == "Custom App"
    assert settings.API_PORT == 9000
    assert settings.DEBUG is False
    assert settings.CLAUDE_MODEL_ID == "custom-model-id"


def test_settings_port_validation():
    """Test that port must be an integer."""
    with pytest.raises(ValueError):
        Settings(API_PORT="not_an_int")


def test_settings_debug_bool_validation():
    """Test that DEBUG is correctly parsed as boolean."""
    settings_true = Settings(DEBUG=True)
    settings_false = Settings(DEBUG=False)

    assert settings_true.DEBUG is True
    assert settings_false.DEBUG is False
