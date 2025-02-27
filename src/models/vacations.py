from sqlalchemy import Column, Integer, String, Numeric, Date, Sequence, ForeignKey
from .base import Base  # Import Base from base.py


class Vacation(Base):
    __tablename__ = 'vacations'
    vacation_id = Column(Integer, Sequence(
        'vacation_id_seq'), primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    description = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    price = Column(Numeric)
    image_name = Column(String(100))
