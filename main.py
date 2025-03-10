from src.dal.vacations_dao import get_all_vacations, create_vacations_table
from src.dal.users_dao import get_all_users, create_users_table
from src.dal.likes_dao import get_all_likes
from src.dal.countries_dao import get_all_countries
from src.dal.roles_dao import get_all_roles
from src.dal.db_conn import get_connection

import time
import pytest
import sys
import psycopg2
import os


def recreate_test_db():
    """Drop and recreate the test database."""
    conn = psycopg2.connect(
        dbname="postgres",  # Connect to the default system database first
        user="admin",  # Use the same credentials as db_conn.py
        password="1234",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS test_db;")
    cursor.execute("CREATE DATABASE test_db;")
    # Ensure admin has access
    cursor.execute("GRANT ALL PRIVILEGES ON DATABASE test_db TO admin;")

    cursor.close()
    conn.close()
    print("Test database recreated successfully.")


def setup_test_tables():
    """Create test tables in test_db."""
    conn = get_connection()  # Connect to test_db
    cursor = conn.cursor()

    create_users_table()
    create_vacations_table()

    cursor.close()
    conn.close()
    print("Test tables created successfully.")


def show_test_data():
    """Display test data after test execution."""
    conn = get_connection()
    cursor = conn.cursor()

    print("\nUsers:")
    users = get_all_users()
    for user in users:
        print(user)

    print("\nLikes:")
    likes = get_all_likes()
    for like in likes:
        print(like)

    print("\nCountries:")
    countries = get_all_countries()
    for country in countries:
        print(country)

    print("\nRoles:")
    roles = get_all_roles()
    for role in roles:
        print(role)

    print("\nVacations:")
    vacations = get_all_vacations()
    for vacation in vacations:
        print(vacation)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    print("Recreating test database...")
    recreate_test_db()
    setup_test_tables()

    print("\nRunning database tests first...\n")
    exit_code = pytest.main(["-v", "-s", "tests/test_db.py"])

    if exit_code != 0:
        sys.exit(exit_code)  # Stop execution if database setup fails

    print("\nRunning all other tests...\n")
    exit_code = pytest.main(["-v", "-s", "tests"])

    if exit_code != 0:
        sys.exit(exit_code)  # Stop execution if tests fail

    print("Restoring vacations data...")
    create_vacations_table()

    show_test_data()

    print("\nAll tests passed!")
