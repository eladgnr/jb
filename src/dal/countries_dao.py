"""
countries_dao.py
================

This module manages database operations related to the `countries` table.
It provides functions to fetch all countries and create the table with initial data.

Functions:
----------
- get_all_countries() -> list:
    Fetches all country records from the database.

- create_countries_table() -> None:
    Creates the `countries` table if it does not exist and populates it with predefined data.
"""
from src.dal.db_conn import get_connection


def get_all_countries():
    """Fetch all countries from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM countries")
        countries = cur.fetchall()
        cur.close()
        conn.close()
        return countries
    return []


def create_countries_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS countries (
                country_id SERIAL PRIMARY KEY,
                country_name VARCHAR(50) UNIQUE NOT NULL,
                description VARCHAR(255) NOT NULL
            )
        """)
        cur.execute("""
            INSERT INTO countries (country_name, description)
            VALUES 
            ('Israel', 'Sunny beaches and Jerusalem.'),
            ('Brazil', 'Home of the Amazon rainforest.'),
            ('Canada', 'Maple syrup and wilderness.'),
            ('China', 'Great Wall and rich history.'),
            ('France', 'Eiffel Tower and wine.'),
            ('Germany', 'Engineering specialties.'),
            ('India', 'Diverse culture and Taj Mahal.'),
            ('Japan', 'shusi and cherry blossoms.'),
            ('South Africa', 'Wildlife and amazing landscapes.'),
            ('United States', 'Big cities and grand canyons.')
            ON CONFLICT (country_name) DO NOTHING
        """)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_countries_table()
