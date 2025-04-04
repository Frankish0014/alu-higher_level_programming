#!/usr/bin/python3
"""Define the State class and its relationship with City."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class definition."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    
    # Relationship with City, delete cities when state is deleted
    cities = relationship('City', backref='state', cascade="all, delete", passive_deletes=True)
