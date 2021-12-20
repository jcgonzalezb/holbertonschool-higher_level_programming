#!/usr/bin/python3
"""
Definition of class City.
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    Class City. inherits from Base; instance of base
    Creates a table "states" and it is linked to MySQL.
    """
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
