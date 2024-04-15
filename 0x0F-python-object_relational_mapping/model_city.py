#!/usr/bin/python3
"""contains the class definition of a State"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


# Create Base instance
Base = declarative_base()


class City(Base):
    """defining a class called State"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
