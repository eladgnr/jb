import pytest
from unittest.mock import patch
from src.services.user_service import UserService


def test_create_user_as_admin():
    """Positive Test: Admin (job_id=2) should be able to create a user."""
    print("Running positive test: test_create_user_as_admin")

    with patch("src.dal.users_dao.create_user", return_value=2) as mock_create_user:
        user_service = UserService(None)
        admin_id = 2
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "password": "securepass",
            "job_id": 1
        }

        new_user_id = user_service.register_user(admin_id, **user_data)

        assert new_user_id is not None
        assert isinstance(new_user_id, int)
        mock_create_user.assert_called_once_with(
            admin_id, "John", "Doe", "john@example.com", "securepass", 1)


def test_create_user_as_non_admin():
    """Negative Test: Non-admin user should NOT be able to create a user."""
    print("Running negative test: test_create_user_as_non_admin")

    with patch("src.dal.users_dao.create_user", side_effect=PermissionError("Only admin users can create new users.")):
        user_service = UserService(None)
        non_admin_id = 3
        user_data = {
            "first_name": "Alice",
            "last_name": "Brown",
            "email": "alice@example.com",
            "password": "securepass",
            "job_id": 1
        }

        with pytest.raises(PermissionError, match="Only admin users can create new users."):
            user_service.register_user(non_admin_id, **user_data)


def test_get_user():
    """Positive Test: Fetch a user by ID."""
    print("Running positive test: test_get_user")

    user_data = {"user_id": 1, "first_name": "Axl",
                 "last_name": "Rose", "email": "axl.rose@example.com"}

    with patch("src.dal.users_dao.get_user_by_id", return_value=user_data) as mock_get_user:
        user_service = UserService(None)
        user = user_service.fetch_user(1)

        assert user["user_id"] == 1
        assert user["first_name"] == "Axl"
        assert user["last_name"] == "Rose"
        assert user["email"] == "axl.rose@example.com"

        mock_get_user.assert_called_once_with(1)


def test_delete_user():
    """Positive Test: Ensure a user can be deleted."""
    print("Running positive test: test_delete_user")

    with patch("src.dal.users_dao.delete_user", return_value=True) as mock_delete:
        user_service = UserService(None)
        result = user_service.delete_user(1)

        assert result is True
        mock_delete.assert_called_once_with(1)
