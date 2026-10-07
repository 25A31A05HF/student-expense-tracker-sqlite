import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/expenses.db")


def get_connection():
    """Create and return a database connection."""
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def create_table():
    """Create the expenses table if it does not already exist."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        """)

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    create_table()
    print("Database and expenses table created successfully.")