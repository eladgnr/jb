from dal.likes_dao import add_like
from models.likes import Like


def like_vacation(user_id, vacation_id):
    new_like = Like(user_id=user_id, vacation_id=vacation_id)
    add_like(new_like)
