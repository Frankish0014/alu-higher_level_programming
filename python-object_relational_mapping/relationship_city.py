#!/usr/bin/python3
"""City class that represents a city linked to a state using SQLAlchemy"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """City class represents a city with a reference to the state it belongs to"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
    def __repr__(self):
        """Return string representation of the City"""
        return f"<City(id={self.id}, name={self.name}, state_id={self.state_id})>"
