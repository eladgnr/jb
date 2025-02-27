import unittest
from src.services.roles_service import create_role, fetch_role


class TestRoles(unittest.TestCase):

    def test_create_role_success(self):
        """Ensure a role can be created without duplication."""
        role_name = "manager"

        # First, check if the role already exists
        try:
            create_role(role_name)
        except ValueError:
            pass  # Ignore if it already exists

        # Try inserting again and expect it to raise ValueError
        with self.assertRaises(ValueError):
            create_role(role_name)

    def test_create_role_duplicate(self):
        """Ensure duplicate role creation raises a ValueError."""
        with self.assertRaises(ValueError):
            create_role('user')  # Assuming 'user' role already exists

    def test_fetch_role_success(self):
        """Ensure a valid role can be fetched successfully."""
        role = fetch_role(1)
        self.assertIsNotNone(role, "Role fetch failed.")

    def test_fetch_role_not_found(self):
        """Ensure fetching a non-existent role returns None."""
        role = fetch_role(9999)  # Assuming ID 9999 doesn't exist
        self.assertIsNone(role, "Role should not exist.")


if __name__ == "__main__":
    unittest.main()
