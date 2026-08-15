import sqlite3
from datetime import datetime

DATABASE_NAME = "travel_concierge.db"


def get_connection():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    """Create the searches table if it does not already exist."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            response TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


def save_search(question: str, response: str):
    """Save a user question and AI response."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO searches (
            question,
            response,
            created_at
        )
        VALUES (?, ?, ?)
        """,
        (
            question,
            response,
            datetime.now().isoformat(timespec="seconds"),
        ),
    )

    connection.commit()
    connection.close()


def get_searches():
    """Return saved searches, newest first."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, question, response, created_at
        FROM searches
        ORDER BY id DESC
        """
    )

    searches = cursor.fetchall()

    connection.close()

    return searches