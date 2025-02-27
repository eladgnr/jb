from dal.users_dao import get_user_by_id, create_user
from models.users import User


def register_user(first_name, last_name, email, password, job_id):
    # Implement business logic for registering a new user
    new_user = User(first_name=first_name, last_name=last_name,
                    email=email, password=password, job_id=job_id)
    create_user(new_user)


def fetch_user(user_id):
    return get_user_by_id(user_id)
