from src.dal import users_dao


class UserService:
    def __init__(self, db):
        self.db = db

    def register_user(self, admin_id, first_name, last_name, email, password, job_id):
        """Creates a new user with admin verification"""
        return users_dao.create_user(admin_id, first_name, last_name, email, password, job_id)

    def fetch_user(self, user_id):
        """Fetches a user by ID"""
        return users_dao.get_user_by_id(user_id)

    def delete_user(self, user_id):
        """Deletes a user by ID"""
        return users_dao.delete_user(user_id)
