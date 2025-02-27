from .db_conn import get_connection  # Fixed import


def create_roles_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE roles (
                job_id SERIAL PRIMARY KEY,
                role_name VARCHAR(50) UNIQUE NOT NULL
            )
        """)
        cur.execute("INSERT INTO roles (role_name) VALUES ('user'), ('admin')")
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_roles_table()
