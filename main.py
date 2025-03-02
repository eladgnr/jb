from src.dal.vacations_dao import get_all_vacations
from src.dal.users_dao import get_all_users


def show_vacations():
    vacations = get_all_vacations()
    if vacations:
        print("\nVacations List:")
        print("=" * 80)
        for vacation in vacations:
            print(
                f"ID: {vacation[0]} | Country ID: {vacation[1]} | {vacation[2]} | {vacation[3]} to {vacation[4]} | Price: ${vacation[5]} | Image: {vacation[6]}")
    else:
        print("No vacations found.")


def show_users():
    users = get_all_users()
    if users:
        print("\nUsers List:")
        print("=" * 80)
        for user in users:
            print(
                f"ID: {user[0]} | Name: {user[1]} {user[2]} | Email: {user[3]} | Role ID: {user[4]}")
    else:
        print("No users found.")


if __name__ == "__main__":
    show_vacations()
    show_users()
