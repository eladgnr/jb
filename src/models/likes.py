from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class Like(Base):
    __tablename__ = 'likes'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    vacation_id = Column(Integer, ForeignKey(
        'vacations.vacation_id'), primary_key=True)
