#!/usr/bin/python3
"""Create a new state and city in the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Create tables (if not already created)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new state "California"
    california = State(name="California")

    # Create a new city "San Francisco" and associate with California
    san_francisco = City(name="San Francisco", state=california)

    # Add and commit to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Print the id of the newly created state and city
    print(f"State created: {california.id}")
    print(f"City created: {san_francisco.id}")
