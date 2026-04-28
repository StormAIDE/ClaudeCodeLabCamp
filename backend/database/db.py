"""
SQLite database for storing article history.
"""
import sqlite3
import os
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class Database:
    """Simple SQLite database for article storage."""

    def __init__(self, db_path: str = "./data/articles.db"):
        """Initialize database connection."""
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_db()

    def init_db(self):
        """Initialize database schema and run idempotent migrations."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                summary TEXT,
                topic TEXT,
                subtopic TEXT DEFAULT 'general',
                published_date TEXT,
                fetched_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        self._migrate_add_subtopic_column(conn)
        conn.close()
        logger.info("Database initialized at %s", self.db_path)

    def _migrate_add_subtopic_column(self, conn: sqlite3.Connection):
        """Safely add subtopic column to existing databases that predate it."""
        cursor = conn.execute("PRAGMA table_info(articles)")
        columns = [row[1] for row in cursor.fetchall()]
        if "subtopic" not in columns:
            logger.info("Migration: adding subtopic column to articles table")
            conn.execute("ALTER TABLE articles ADD COLUMN subtopic TEXT DEFAULT 'general'")
            conn.commit()
            logger.info("Migration complete: subtopic column added")

    def add_article(self, title: str, url: str, summary: str, topic: str, published_date: str):
        """Add a tech news article to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO articles (title, url, summary, topic, published_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, url, summary, topic, published_date))

        conn.commit()
        conn.close()
        logger.info("Added article: %s", title)

    def add_robotics_article(
        self,
        title: str,
        url: str,
        summary: str,
        subtopic: str,
        published_date: str,
    ):
        """Add a robotics article with subtopic tag."""
        from backend.tools.robotics_tools import ROBOTICS_SUBTOPICS
        safe_subtopic = subtopic if subtopic in ROBOTICS_SUBTOPICS else "general"

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO articles (title, url, summary, topic, subtopic, published_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, url, summary, "robotics", safe_subtopic, published_date))

        conn.commit()
        conn.close()
        logger.info("Added robotics article [%s]: %s", safe_subtopic, title)

    def get_articles_by_topic(self, topic: str, limit: int = 10) -> List[Dict]:
        """Get articles for a specific topic."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, title, url, summary, topic, subtopic, published_date, fetched_at
            FROM articles
            WHERE topic LIKE ?
            ORDER BY fetched_at DESC
            LIMIT ?
        ''', (f'%{topic}%', limit))

        columns = ['id', 'title', 'url', 'summary', 'topic', 'subtopic', 'published_date', 'fetched_at']
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        conn.close()
        return results

    def get_robotics_articles(self, subtopic: Optional[str] = None, limit: int = 10) -> List[Dict]:
        """Get robotics articles. Pass subtopic=None to return all robotics articles."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if subtopic is None:
            cursor.execute('''
                SELECT id, title, url, summary, topic, subtopic, published_date, fetched_at
                FROM articles
                WHERE topic = 'robotics'
                ORDER BY fetched_at DESC
                LIMIT ?
            ''', (limit,))
        else:
            cursor.execute('''
                SELECT id, title, url, summary, topic, subtopic, published_date, fetched_at
                FROM articles
                WHERE topic = 'robotics' AND subtopic = ?
                ORDER BY fetched_at DESC
                LIMIT ?
            ''', (subtopic, limit))

        columns = ['id', 'title', 'url', 'summary', 'topic', 'subtopic', 'published_date', 'fetched_at']
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        conn.close()
        return results

    def search_articles(self, query: str, days: int = 7, limit: int = 10, minutes: int = 10) -> List[Dict]:
        """Full-text search across all cached articles."""
        cutoff = (datetime.now() - timedelta(minutes=minutes)).isoformat()
        pattern = f"%{query}%"
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                """SELECT id, title, url, summary, topic, fetched_at, published_date
                   FROM articles
                   WHERE (title LIKE ? OR summary LIKE ?)
                     AND fetched_at > ?
                   ORDER BY fetched_at DESC
                   LIMIT ?""",
                (pattern, pattern, cutoff, limit)
            )
            return [dict(row) for row in cursor.fetchall()]

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
