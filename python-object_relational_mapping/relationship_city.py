#!/usr/bin/python3
"""Define the City class linked to the State class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base

class City(Base):
    """City class definition."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id', ondelete='CASCADE'), nullable=False)

    # Relationship to the State class (this allows referencing the state from city)
    state = relationship("State", backref="cities")
