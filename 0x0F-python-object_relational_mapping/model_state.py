#!/usr/bin/python3
"""
Definition of class State.
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Class State. inherits from Base; instance of base
    Creates a table "states" and it is linked to MySQL.
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
