import sqlite3

DATABASE_NAME = "urls.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_code TEXT UNIQUE,
        original_url TEXT,
        clicks INTEGER DEFAULT 0,
        expires_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_url(short_code, original_url, expires_at):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO urls
        (short_code, original_url, expires_at)
        VALUES (?, ?, ?)
        """,
        (short_code, original_url, expires_at)
    )

    conn.commit()
    conn.close()


def get_url(short_code):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT original_url, expires_at
        FROM urls
        WHERE short_code = ?
        """,
        (short_code,)
    )

    result = cursor.fetchone()

    conn.close()

    return result


def get_existing_url(original_url):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT short_code, expires_at
        FROM urls
        WHERE original_url = ?
        """,
        (original_url,)
    )

    result = cursor.fetchone()

    conn.close()

    return result