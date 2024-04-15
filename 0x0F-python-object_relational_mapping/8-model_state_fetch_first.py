#!/usr/bin/python3
"""script that lists first State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """function listing first states"""
    # Create engine
    engine = create_engine(f"mysql://{username}:{password}\
                            @localhost:3306/{database}")

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and sort states by id
    states = session.query(State).first()

    # Display results
    if not states:
        print("Nothing")
    else:
        print(f"{states.id}: {states.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to list states
    list_states(username, password, database)
