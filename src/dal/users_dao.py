"""
This module manages database operations related to the `users` table.
It provides functions for fetching, inserting, updating, and deleting user records.

Functions:
----------
- get_user_by_id(user_id: int) -> dict | None:
    Fetches a user by ID and returns it as a dictionary. Returns `None` if not found.

- get_all_users() -> list:
    Fetches all users from the database.

- create_users_table() -> None:
    Drops and recreates the `users` table, then inserts default users.

- create_user(admin_id: int, first_name: str, last_name: str, email: str, password: str, job_id: int) -> int:
    Creates a new user if the caller is an admin (`job_id=2`). Raises `PermissionError` if unauthorized.

- delete_user(user_id: int) -> bool:
    Deletes a user by ID. Returns `True` if successful, otherwise `False`.
"""
from src.dal.db_conn import get_connection


def get_user_by_id(user_id):
    """Fetch a user by ID from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return dict(zip(["user_id", "first_name", "last_name", "email", "password", "job_id"], user)) if user else None
    return None


def get_all_users():
    """Fetch all users from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users
    return []


def create_users_table():
    """Drop and recreate the users table before inserting default users."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS users CASCADE")

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
            ('Axl', 'Rose', 'axl.rose@example.com', 'pass123', 1),
            ('Steve', 'Vai', 'steve.vai@example.com', 'pass123', 2),
            ('Eric', 'Clapton', 'eric.clapton@example.com', 'pass123', 1),
            ('David', 'Gilmour', 'david.gilmoure@example.com', 'pass123', 2),
            ('Elton', 'John', 'elton.john@example.com', 'pass123', 1)
            ON CONFLICT (email) DO NOTHING
        """)

        conn.commit()
        cur.close()
        conn.close()


def create_user(admin_id, first_name, last_name, email, password, job_id):
    """Only allow admin users to create new users."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()

        # Check if the caller is an admin
        cur.execute("SELECT job_id FROM users WHERE user_id = %s", (admin_id,))
        admin_role = cur.fetchone()

        if not admin_role or admin_role[0] != 2:
            cur.close()
            conn.close()
            raise PermissionError("Only admin users can create new users.")

        # Proceed with user creation
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


def delete_user(user_id):
    """Delete a user by their ID."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM users WHERE user_id = %s RETURNING user_id;", (user_id,))
        deleted_user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return deleted_user is not None  # Return True if deletion was successful
    return False


if __name__ == "__main__":
    create_users_table()
