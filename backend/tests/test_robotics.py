"""
Unit tests for robotics news endpoints and tools.
"""
import pytest
from unittest.mock import patch, MagicMock
from fastapi import status
from backend.tools.robotics_tools import (
    ROBOTICS_SUBTOPICS,
    search_robotics_news,
    fetch_robotics_articles,
)


# ── Tool-level tests ──────────────────────────────────────────────────────────

def test_robotics_subtopics_list():
    """ROBOTICS_SUBTOPICS contains exactly the expected 6 values."""
    expected = {"general", "humanoids", "drones", "ros", "research", "industrial"}
    assert set(ROBOTICS_SUBTOPICS) == expected
    assert len(ROBOTICS_SUBTOPICS) == 6


def test_search_robotics_news_invalid_subtopic():
    """search_robotics_news returns an error string for invalid subtopic."""
    result = search_robotics_news(subtopic="invalid_topic")
    assert "Invalid subtopic" in result
    assert "invalid_topic" in result


def test_search_robotics_news_injection_attempt():
    """search_robotics_news rejects SQL-like injection strings."""
    result = search_robotics_news(subtopic="'; DROP TABLE articles; --")
    assert "Invalid subtopic" in result


def test_search_robotics_news_valid_subtopic_with_cache():
    """search_robotics_news uses cached articles when available."""
    fake_articles = [
        {
            "id": i,
            "title": f"Robot News {i}",
            "url": f"https://example.com/{i}",
            "summary": "A robotics article.",
            "topic": "robotics",
            "subtopic": "humanoids",
            "published_date": "2026-04-20T10:00:00",
            "fetched_at": "2026-04-20T11:00:00",
        }
        for i in range(5)
    ]

    with patch('backend.database.db.db') as mock_db:
        mock_db.get_robotics_articles.return_value = fake_articles
        result = search_robotics_news(subtopic="humanoids")

    assert "humanoids" in result
    assert "Found" in result


def test_search_robotics_news_fetches_when_no_cache():
    """search_robotics_news fetches fresh articles when cache is empty."""
    with patch('backend.database.db.db') as mock_db, \
         patch('backend.tools.robotics_tools.fetch_robotics_articles') as mock_fetch:

        mock_db.get_robotics_articles.return_value = []
        mock_fetch.return_value = [
            {
                "title": "Drone Report",
                "url": "https://example.com/drone",
                "summary": "Latest drone news.",
                "published_date": "2026-04-20T10:00:00",
                "subtopic": "drones",
            }
        ]

        result = search_robotics_news(subtopic="drones")

    assert "drones" in result
    mock_fetch.assert_called_once_with("drones", 7)


# ── API endpoint tests ────────────────────────────────────────────────────────

def test_get_robotics_subtopics(test_client):
    """GET /api/v1/robotics/subtopics returns the expected list."""
    response = test_client.get("/api/v1/robotics/subtopics")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert "general" in data
    assert "humanoids" in data
    assert len(data) == 6


def test_get_robotics_news_default_subtopic(test_client):
    """GET /api/v1/robotics with no subtopic param returns all robotics articles."""
    fake_articles = [{"id": 1, "title": "Test", "url": "https://x.com", "summary": "s",
                      "topic": "robotics", "subtopic": "general",
                      "published_date": None, "fetched_at": None}]
    with patch('backend.api.endpoints.robotics.db') as mock_db:
        mock_db.get_robotics_articles.return_value = fake_articles
        response = test_client.get("/api/v1/robotics")

    assert response.status_code == status.HTTP_200_OK
    mock_db.get_robotics_articles.assert_called_once_with(subtopic=None, limit=20)


def test_get_robotics_news_valid_subtopic(test_client):
    """GET /api/v1/robotics?subtopic=drones returns articles."""
    fake_article = {
        "id": 1,
        "title": "Drone Tech Update",
        "url": "https://example.com/drone",
        "summary": "Summary here.",
        "topic": "robotics",
        "subtopic": "drones",
        "published_date": "2026-04-20",
        "fetched_at": "2026-04-20T12:00:00",
    }
    with patch('backend.api.endpoints.robotics.db') as mock_db:
        mock_db.get_robotics_articles.return_value = [fake_article]
        response = test_client.get("/api/v1/robotics?subtopic=drones")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["subtopic"] == "drones"


def test_get_robotics_news_invalid_subtopic(test_client):
    """GET /api/v1/robotics?subtopic=invalid returns 400."""
    response = test_client.get("/api/v1/robotics?subtopic=invalid_topic")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Invalid subtopic" in response.json()["detail"]


def test_get_robotics_news_limit_too_high(test_client):
    """GET /api/v1/robotics?limit=999 returns 422 (validation error)."""
    response = test_client.get("/api/v1/robotics?limit=999")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_get_robotics_news_db_error(test_client):
    """GET /api/v1/robotics returns 500 on database error."""
    with patch('backend.api.endpoints.robotics.db') as mock_db:
        mock_db.get_robotics_articles.side_effect = RuntimeError("DB crashed")
        response = test_client.get("/api/v1/robotics")

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
