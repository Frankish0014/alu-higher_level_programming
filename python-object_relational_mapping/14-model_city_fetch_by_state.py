#!/usr/bin/python3
"""Fetch and display all City objects from the database, sorted by city id."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and join with states to fetch state names
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display results as requested
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
