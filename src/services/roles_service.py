from src.dal.roles_dao import get_role_by_id, create_role


def fetch_role(role_id):
    """Fetch a role by its ID."""
    return get_role_by_id(role_id)


def add_role(role_name):
    """Add a new role to the database."""
    return create_role(role_name)
