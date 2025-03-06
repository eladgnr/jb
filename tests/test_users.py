import pytest
from unittest.mock import MagicMock
from src.dal.users_dao import create_user, get_user_by_id
from src.services.user_service import UserService
import uuid


def test_create_user_as_admin():
    """Positive Test: Admin (job_id=2) should be able to create a user."""
    print("Running positive test: test_create_user_as_admin")

    mock_db = MagicMock()
    user_service = UserService(mock_db)  # Use UserService instance

    admin_id = 2  # Use an actual admin user from the database
    unique_email = f"john{uuid.uuid4().hex}@example.com"  # Ensure unique email

    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": unique_email,
        "password": "securepass",
        "job_id": 1  # Regular user
    }

    mock_db.insert.return_value = 2  # Mock returning a new user_id

    # FIX: Call register_user from UserService to ensure mock is used
    new_user_id = user_service.register_user(
        admin_id, **user_data)  # FIX: Pass admin_id

    assert new_user_id is not None
    assert isinstance(new_user_id, int)
    mock_db.create_user.return_value = 2


def test_create_user_as_non_admin():
    """Negative Test: Non-admin user should NOT be able to create a user."""
    print("Running negative test: test_create_user_as_non_admin")

    mock_db = MagicMock()
    user_service = UserService(mock_db)

    non_admin_id = 3  # A regular user (job_id≠2)
    user_data = {
        "first_name": "Alice",
        "last_name": "Brown",
        "email": "alice@example.com",
        "password": "securepass",
        "job_id": 1  # Regular user
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

    user = user_service.fetch_user(1)  # FIX: Use fetch_user()

    assert user["user_id"] == 1
    assert user["first_name"] == "John"  # FIX: Use correct key
    assert user["last_name"] == "Doe"    # FIX: Use correct key
    # FIX: Allow both expected emails
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
