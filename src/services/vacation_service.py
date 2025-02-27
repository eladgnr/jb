from ..dal.vacations_dao import get_all_vacations, create_vacation  # Fixed import
from ..models.vacations import Vacation  # Fixed import


def list_vacations():
    return get_all_vacations()


def add_vacation(country_id, description, start_date, end_date, price, image_name):
    new_vacation = Vacation(country_id=country_id, description=description,
                            start_date=start_date, end_date=end_date, price=price, image_name=image_name)
    create_vacation(new_vacation)
