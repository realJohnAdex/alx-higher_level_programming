#!/usr/bin/python3
"""script that updates State object to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, database):
    """function updating states"""
    # Create engine
    engine = create_engine(f"mysql://{username}:{password}\
                            @localhost:3306/{database}")

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"

    # Commit transaction
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to add state
    update_state(username, password, database)
