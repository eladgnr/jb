from src.dal.users_dao import get_user_by_id, create_user
from src.models.users import User


class UserService:
    def __init__(self, db):
        """Initialize UserService with a database connection."""
        self.db = db  # Store database dependency

    def register_user(self, admin_id, first_name, last_name, email, password, job_id):
        """Creates a new user with admin verification"""
        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, password=password, job_id=job_id)
        # FIX: Pass admin_id
        return create_user(admin_id, first_name, last_name, email, password, job_id)

    def fetch_user(self, user_id):
        """Fetches a user by ID"""
        return self.db.get_user_by_id(user_id)

    def delete_user(self, user_id):
        """Deletes a user by ID"""
        return self.db.delete(user_id)  # FIX: Add this method
