#!/usr/bin/python3
"""contains the class definition of a State"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Create Base instance
Base = declarative_base()


class State(Base):
    """defining a class called State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
