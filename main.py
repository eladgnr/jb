from src.dal.vacations_dao import get_all_vacations, create_vacations_table
from src.dal.users_dao import get_all_users, create_users_table
from src.dal.likes_dao import get_all_likes
from src.dal.countries_dao import get_all_countries
from src.dal.roles_dao import get_all_roles
import pytest
import sys


def show_vacations():
    vacations = get_all_vacations()
    if vacations:
        print("\nVacations List:")
        print("=" * 100)
        for vacation in vacations:
            print(
                f"ID: {vacation[0]} | Country ID: {vacation[1]} | {vacation[2]} | {vacation[3]} to {vacation[4]} | Price: ${vacation[5]} | Image: {vacation[6]}")
    else:
        print("No vacations found.")


def show_users():
    users = get_all_users()
    if users:
        print("\nUsers List:")
        print("=" * 100)
        for user in users:
            print(
                f"ID: {user[0]} | Name: {user[1]} {user[2]} | Email: {user[3]} | Role ID: {user[5]}")
    else:
        print("No users found.")


def show_likes():
    likes = get_all_likes()
    if likes:
        print("\nLikes List:")
        print("=" * 100)
        for like in likes:
            print(
                f"ID: {like[0]} | User ID: {like[1]} | Vacation ID: {like[2]}")
    else:
        print("No likes found.")


def show_countries():
    countries = get_all_countries()
    if countries:
        print("\nCountries List:")
        print("=" * 100)
        for country in countries:
            print(f"ID: {country[0]} | Name: {country[1]}")
    else:
        print("No countries found.")


def show_roles():
    roles = get_all_roles()
    if roles:
        print("\nRoles List:")
        print("=" * 100)
        for role in roles:
            print(f"ID: {role[0]} | Role Name: {role[1]}")
    else:
        print("No roles found.")


if __name__ == "__main__":
    print("Recreating vacations table...")
    create_vacations_table()

    print("Recreating users table...")
    create_users_table()

    print("\nRunning tests...\n")
    exit_code = pytest.main(
        ["-v", "-s", "tests/test_vacations.py", "tests/test_users.py"])

    if exit_code != 0:
        sys.exit(exit_code)  # Stop execution if tests fail

    show_vacations()
    show_users()
    show_likes()
    show_countries()
    show_roles()
