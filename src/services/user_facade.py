from ..dal.db_conn import get_connection  # Fixed import


def create_user(first_name, last_name, email, password, job_id):
    if email_exists(email):
        raise ValueError("Email already exists.")

    if not all([first_name, last_name, email, password, job_id]):
        raise ValueError("All fields are required.")

    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long.")

    try:
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
    except Exception as e:
        print(f"Database error: {e}")


def email_exists(email):
    try:
        conn = get_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(
                "SELECT COUNT(*) FROM users WHERE email = %s", (email,))
            count = cur.fetchone()[0]
            cur.close()
            conn.close()
            return count > 0
    except Exception as e:
        print(f"Database error: {e}")
        return False


def login_user(email, password):
    if not email or not password:
        raise ValueError("Email and password are required.")

    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long.")

    try:
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
    except Exception as e:
        print(f"Database error: {e}")
        return None
