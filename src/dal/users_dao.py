from src.dal.db_conn import get_connection  # Works with direct execution


def get_user_by_id(user_id):
    """Fetch a user by ID from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user  # Returns None if no user found
    return None


def get_all_users():
    """Fetch all users from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")  # Fetch all user records
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users  # Returns a list of tuples
    return []


def create_users_table():
    """Create the users table and insert default users."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
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
            ('John', 'Doe', 'john.doe@example.com', 'pass123', 1),
            ('Jane', 'Smith', 'jane.smith@example.com', 'pass123', 2),
            ('Alice', 'Brown', 'alice.brown@example.com', 'pass123', 1),
            ('Bob', 'Johnson', 'bob.johnson@example.com', 'pass123', 2),
            ('Eve', 'Davis', 'eve.davis@example.com', 'pass123', 1)
            ON CONFLICT (email) DO NOTHING
        """)
        conn.commit()
        cur.close()
        conn.close()


def create_user(first_name, last_name, email, password, job_id):
    """Insert a new user into the users table."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (first_name, last_name, email, password, job_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING user_id;
        """, (first_name, last_name, email, password, job_id))

        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return user_id  # Return the new user ID
    return None


if __name__ == "__main__":
    create_users_table()
