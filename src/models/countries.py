from sqlalchemy import Column, Integer, String, Sequence
from .base import Base  # Import Base from base.py


class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, Sequence('country_id_seq'), primary_key=True)
    country_name = Column(String(50), nullable=False)
    description = Column(String(255))
