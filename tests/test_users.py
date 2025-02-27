import pytest
from unittest.mock import MagicMock
from src.models.users import User
from src.services.user_service import UserService


def test_create_user():
    mock_db = MagicMock()
    user_service = UserService(mock_db)

    user_data = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    mock_db.insert.return_value = user_data

    new_user = user_service.create_user(user_data)

    assert new_user["id"] == 1
    assert new_user["name"] == "John Doe"
    assert new_user["email"] == "john@example.com"
    mock_db.insert.assert_called_once()


def test_get_user():
    mock_db = MagicMock()
    user_service = UserService(mock_db)

    user_data = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    mock_db.get_by_id.return_value = user_data

    user = user_service.get_user(1)

    assert user["id"] == 1
    assert user["name"] == "John Doe"
    assert user["email"] == "john@example.com"
    mock_db.get_by_id.assert_called_once_with(1)


def test_delete_user():
    mock_db = MagicMock()
    user_service = UserService(mock_db)

    mock_db.delete.return_value = True
    result = user_service.delete_user(1)

    assert result is True
    mock_db.delete.assert_called_once_with(1)
