#!/usr/bin/python3
"""script that adds State object to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database):
    """function adding “Louisiana" to states"""
    # Create engine
    engine = create_engine(f"mysql://{username}:{password}\
                            @localhost:3306/{database}")

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create state object
    new_state = State(name="Louisiana")

    # Add to the session and commit transaction
    session.add(new_state)
    session.commit()
    print(new_state.id)

    # Close session
    session.close()


if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to add state
    add_state(username, password, database)
