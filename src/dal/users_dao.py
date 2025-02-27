from .db_conn import get_connection  # Fixed import


def create_users_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE users (
                user_id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                job_id INTEGER REFERENCES roles(job_id)
            )
        """)
        cur.execute("""
            INSERT INTO users (first_name, last_name, email, password, job_id) 
            VALUES 
            ('John', 'Doe', 'john.doe@example.com', 'password123', 1),
            ('Jane', 'Smith', 'jane.smith@example.com', 'password123', 2)
        """)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_users_table()
