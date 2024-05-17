from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fullname = Column(String(30), nullable=False)
    email = Column(String(40), nullable=False)
    phone_number = Column(String(13), nullable=False)
    birthday = Column(Date, nullable=False)
    description = Column(String(150))
    created_at = Column('created_at', DateTime, default=func.now())
