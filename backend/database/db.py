"""
SQLite database for storing article history.
"""
import sqlite3
import os
from typing import List, Dict
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class Database:
    """Simple SQLite database for article storage."""

    def __init__(self, db_path: str = "./data/articles.db"):
        """Initialize database connection."""
        self.db_path = db_path
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_db()

    def init_db(self):
        """Initialize database schema."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                summary TEXT,
                topic TEXT,
                published_date TEXT,
                fetched_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()
        logger.info(f"Database initialized at {self.db_path}")

    def add_article(self, title: str, url: str, summary: str, topic: str, published_date: str):
        """Add an article to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO articles (title, url, summary, topic, published_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, url, summary, topic, published_date))

        conn.commit()
        conn.close()
        logger.info(f"Added article: {title}")

    def get_articles_by_topic(self, topic: str, limit: int = 10) -> List[Dict]:
        """Get articles for a specific topic."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, title, url, summary, topic, published_date, fetched_at
            FROM articles
            WHERE topic LIKE ?
            ORDER BY fetched_at DESC
            LIMIT ?
        ''', (f'%{topic}%', limit))

        columns = ['id', 'title', 'url', 'summary', 'topic', 'published_date', 'fetched_at']
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        conn.close()
        return results

    def get_trending_topics(self, days: int = 7, limit: int = 5) -> List[Dict]:
        """Get trending topics based on article counts."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT topic, COUNT(*) as count
            FROM articles
            WHERE fetched_at >= datetime('now', ? || ' days')
            GROUP BY topic
            ORDER BY count DESC
            LIMIT ?
        ''', (f'-{days}', limit))

        results = [{'topic': row[0], 'count': row[1]} for row in cursor.fetchall()]

        conn.close()
        return results


# Global database instance
db = Database()
