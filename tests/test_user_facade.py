from unittest.mock import MagicMock
from src.services.user_facade import UserFacade


def test_create_user():
    mock_service = MagicMock()
    facade = UserFacade()
    facade.user_service = mock_service

    facade.register_user(2, "Alice", "Wonderland",
                         "alice@example.com", "pass123", 1)
    mock_service.register_user.assert_called_once()


def test_login_user():
    mock_service = MagicMock()
    mock_service.fetch_user_by_email.return_value = {
        "email": "alice@example.com", "password": "pass123"
    }

    facade = UserFacade()
    facade.user_service = mock_service

    user = facade.login_user("alice@example.com", "pass123")
    assert user["email"] == "alice@example.com"
