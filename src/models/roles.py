from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'
    job_id = Column(Integer, Sequence('job_id_seq'), primary_key=True)
    role_name = Column(String(50), unique=True, nullable=False)
