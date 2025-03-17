"""
likes_dao.py
============

This module manages database operations related to the `likes` table.
It provides functions to create the table, fetch all likes, and add new likes.

Functions:
----------
- get_all_likes() -> list:
    Fetches all likes from the database.

- create_likes_table() -> None:
    Creates the `likes` table if it does not exist.

- add_like(user_id: int, vacation_id: int) -> None:
    Inserts a new like into the `likes` table.

Usage Example:
--------------
>>> from src.dal.likes_dao import get_all_likes, add_like
>>> likes = get_all_likes()
>>> print(likes)

>>> add_like(1, 3)  # User 1 likes vacation 3
"""

from src.dal.db_conn import get_connection


def get_all_likes():
    """Fetch all likes from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM likes")
        likes = cur.fetchall()
        cur.close()
        conn.close()
        return likes
    return []


def create_likes_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS likes (
                user_id INTEGER REFERENCES users(user_id),
                vacation_id INTEGER REFERENCES vacations(vacation_id),
                PRIMARY KEY (user_id, vacation_id)
            )
        """)
        conn.commit()
        cur.close()
        conn.close()


def add_like(user_id, vacation_id):
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)",
                (user_id, vacation_id)
            )
            conn.commit()
        finally:
            cur.close()
            conn.close()


if __name__ == "__main__":
    create_likes_table()
