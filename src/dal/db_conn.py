"""
db_conn.py
==========

This module handles database connectivity for the application.
It provides a function to establish a connection to the PostgreSQL database.

Functions:
----------
- get_connection() -> psycopg2.extensions.connection | None:
    Establishes and returns a connection to the PostgreSQL database.
    If the connection fails, it prints an error message and returns `None`.
"""
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
