from src.services.user_service import UserService
from src.dal.db_conn import get_connection


class UserFacade:
    def __init__(self):
        self.user_service = UserService(
            get_connection())

    def register_user(self, admin_id, first_name, last_name, email, password, job_id):
        """Facade method to create a user with admin validation."""
        return self.user_service.register_user(admin_id, first_name, last_name, email, password, job_id)

    def login_user(self, email, password):
        """Facade method for user authentication."""
        user = self.user_service.fetch_user_by_email(email)
        if user and user["password"] == password:
            return user
        raise ValueError("Invalid email or password.")

    def get_user(self, user_id):
        """Facade method to fetch user details."""
        return self.user_service.fetch_user(user_id)

    def delete_user(self, user_id):
        """Facade method to remove a user."""
        return self.user_service.delete_user(user_id)
