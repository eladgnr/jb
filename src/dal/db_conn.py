import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="admin",
            password="1234",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
