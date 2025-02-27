from .db_conn import get_connection  # Fixed import


def create_likes_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE likes (
                user_id INTEGER REFERENCES users(user_id),
                vacation_id INTEGER REFERENCES vacations(vacation_id),
                PRIMARY KEY (user_id, vacation_id)
            )
        """)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_likes_table()
