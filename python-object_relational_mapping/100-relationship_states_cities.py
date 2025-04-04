#!/usr/bin/python3
"""Script that creates a State "California" and a City "San Francisco" in the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_state import Base
import sys

if __name__ == "__main__":
    # Getting arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db_name}", pool_pre_ping=True)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add objects to the session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Query to verify if the data is inserted
    result = session.query(State).filter(State.name == "California").first()
    if result:
        print(f"{result.name}: {result.cities[0].name}")

    session.close()
