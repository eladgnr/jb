# Ensure this comes after path modification
from services.user_facade import create_user, login_user
import sys
import os
# Add the 'src' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_create_user():
    try:
        create_user('Alice', 'Wonderland',
                    'alice@example.com', 'password123', 1)
        print("User creation test passed.")
    except ValueError as e:
        print(f"User creation test failed: {e}")


def test_login_user():
    try:
        user = login_user('alice@example.com', 'password123')
        print(f"User login test passed: {user}")
    except ValueError as e:
        print(f"User login test failed: {e}")


if __name__ == "__main__":
    test_create_user()
    test_login_user()
