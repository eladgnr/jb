import pytest
from unittest.mock import MagicMock
from src.dal.users_dao import create_user, get_user_by_id
from src.services.user_service import UserService
import uuid


def test_create_user_as_admin():
    """Positive Test: Admin (job_id=2) should be able to create a user."""
    print("Running positive test: test_create_user_as_admin")

    mock_db = MagicMock()
    user_service = UserService(mock_db)

    admin_id = 2
    unique_email = f"john{uuid.uuid4().hex}@example.com"

    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": unique_email,
        "password": "securepass",
        "job_id": 1
    }

    mock_db.insert.return_value = 2

    new_user_id = user_service.register_user(
        admin_id, **user_data)

    assert new_user_id is not None
    assert isinstance(new_user_id, int)
    mock_db.create_user.return_value = 2


def test_create_user_as_non_admin():
    """Negative Test: Non-admin user should NOT be able to create a user."""
    print("Running negative test: test_create_user_as_non_admin")

    mock_db = MagicMock()
    user_service = UserService(mock_db)

    non_admin_id = 3
    user_data = {
        "first_name": "Alice",
        "last_name": "Brown",
        "email": "alice@example.com",
        "password": "securepass",
        "job_id": 1
    }

    with pytest.raises(PermissionError, match="Only admin users can create new users."):
        create_user(non_admin_id, **user_data)


def test_get_user():
    """Positive Test: Fetch a user by ID."""
    print("Running positive test: test_get_user")

    mock_db = MagicMock()
    user_service = UserService(mock_db)

    user_data = {"user_id": 1, "first_name": "John",
                 "last_name": "Doe", "email": "john@example.com"}
    mock_db.get_user_by_id.return_value = user_data

    user = user_service.fetch_user(1)

    assert user["user_id"] == 1
    assert user["first_name"] == "John"
    assert user["last_name"] == "Doe"
    assert user["email"] in ["john@example.com", "john.doe@example.com"]

    mock_db.get_user_by_id.assert_called_once_with(1)


def test_delete_user():
    """Positive Test: Ensure a user can be deleted."""
    print("Running positive test: test_delete_user")

    mock_db = MagicMock()
    user_service = UserService(mock_db)

    mock_db.delete.return_value = True
    result = user_service.delete_user(1)

    assert result is True
    mock_db.delete.assert_called_once_with(1)
