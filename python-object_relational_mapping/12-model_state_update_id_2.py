#!/usr/bin/python3
"""
Updates the name of the State object with id = 2 to 'New Mexico'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extract connection credentials from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Set up the engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get state with id = 2
    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()
