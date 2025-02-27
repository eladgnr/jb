from dal.db_conn import get_connection
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def create_user(first_name, last_name, email, password, job_id):
    # Check if email already exists
    if email_exists(email):
        raise ValueError("Email already exists.")

    # Check if all fields are provided
    if not all([first_name, last_name, email, password, job_id]):
        raise ValueError("All fields are required.")

    # Check password length
    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long.")

    # Create a new user
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (first_name, last_name, email, password, job_id) 
            VALUES (%s, %s, %s, %s, %s)
        """, (first_name, last_name, email, password, job_id))
        conn.commit()
        cur.close()
        conn.close()
        print("User created successfully.")


def email_exists(email):
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return count > 0


def login_user(email, password):
    # Check if email and password are provided
    if not email or not password:
        raise ValueError("Email and password are required.")

    # Check password length
    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long.")

    # Verify user credentials
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            print("Login successful.")
            return user
        else:
            raise ValueError("Invalid email or password.")
