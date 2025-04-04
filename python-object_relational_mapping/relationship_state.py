#!/usr/bin/python3
"""State class that represents a state and its related cities using SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from model_state import Base

class State(Base):
    """State class represents a state with related cities"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    # Relationship to City class
    cities = relationship('City', backref='state', cascade="all, delete-orphan")

    def __repr__(self):
        """Return string representation of the State"""
        return f"<State(id={self.id}, name={self.name})>"
