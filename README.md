# Elad's Project

## Overview
This project is a BE project that using Postgres as the database. (the subject is Vacations)

Built using:
- **Python** with `psycopg2` and `SQLAlchemy`
- **PostgreSQL** for database management
- **pytest** for unit testing

## Setup Instructions

### 🔹 1. Install Dependencies
bash
pip install -r requirements.txtEnsure PostgreSQL

sql
Ensure PostgreSQL is running. Then, create the test database:
CREATE DATABASE test_db;
GRANT ALL PRIVILEGES ON DATABASE test_db TO admin;

bash
python main.py
pytest


Project
├── src
│   ├── dal          # Data Access Layer (Database)
│   ├── models       # Database Models (SQLAlchemy)
│   ├── services     # Business Logic
│   ├── config.py    # Database Configurations
├── tests            # Unit Tests
├── main.py          # Runs the application & tests
├── requirements.txt # Dependencies
├── .gitignore       # Ignore unnecessary files
└── README.md        # Project Documentation

Note:
the system automatically recreates the test database before running tests