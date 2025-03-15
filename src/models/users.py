from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from .base import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    job_id = Column(Integer, ForeignKey('roles.job_id'))
