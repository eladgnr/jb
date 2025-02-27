import sys
import os
import unittest
from src.services.user_facade import create_user, login_user

# Ensure the `src` directory is in the path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')))


class TestUserFacade(unittest.TestCase):

    def test_create_user(self):
        try:
            create_user('Alice', 'Wonderland',
                        'alice@example.com', 'password123', 1)
        except ValueError as e:
            self.fail(f"User creation failed: {e}")

    def test_login_user(self):
        try:
            user = login_user('alice@example.com', 'password123')
            self.assertIsNotNone(user, "Login failed, user not found.")
        except ValueError as e:
            self.fail(f"Login failed: {e}")


if __name__ == "__main__":
    unittest.main()
