from src.dal.db_conn import get_connection  # Works with direct execution


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
