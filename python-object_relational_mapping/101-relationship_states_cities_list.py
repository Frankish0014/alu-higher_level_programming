#!/usr/bin/python3
"""Lists all State objects and corresponding City objects from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Take command-line arguments: mysql username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and their related cities using one query with joinedload
    states = session.query(State).options(joinedload(State.cities)).order_by(State.id, City.id).all()

    # Iterate through states and cities, displaying them as requested
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
