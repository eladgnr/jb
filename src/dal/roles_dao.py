"""
roles_dao.py
============

This module manages database operations related to the `roles` table.
It provides functions to fetch all roles, retrieve a role by ID, and create new roles.

Functions:
----------
- get_all_roles() -> list:
    Fetches all roles from the database.

- get_role_by_id(role_id: int) -> tuple | None:
    Fetches a role by its job ID. Returns `None` if not found.

- create_role(role_name: str) -> int:
    Inserts a new role into the database and returns the generated job ID.
    Raises a `ValueError` if the role already exists.
"""
import psycopg2
from src.dal.db_conn import get_connection


def get_all_roles():
    """Fetch all roles from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM roles")
        roles = cur.fetchall()
        cur.close()
        conn.close()
        return roles
    return []


def get_role_by_id(role_id):
    """Fetch a role by its ID from the database."""
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM roles WHERE job_id = %s", (role_id,))
        role = cur.fetchone()
        cur.close()
        conn.close()
        return role
    return None


def create_role(role_name):
    """Insert a new role into the database, handling duplicates."""
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO roles (role_name)
                VALUES (%s)
                RETURNING job_id;
            """, (role_name,))
            role_id = cur.fetchone()[0]
            conn.commit()
            return role_id
        except psycopg2.errors.UniqueViolation:
            conn.rollback() 
            raise ValueError(f"Role '{role_name}' already exists.")
        finally:
            cur.close()
            conn.close()
