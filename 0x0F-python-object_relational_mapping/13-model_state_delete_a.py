#!/usr/bin/python3
"""script that deletes all State objects contain the letter a
from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states(username, password, database):
    """function deleting all states with a"""
    # Create engine
    engine = create_engine(f"mysql://{username}:{password}\
                            @localhost:3306/{database}")

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and sort states by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    if states:
        [session.delete(state) for state in states if 'a' in state.name]

    # Commit transaction
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to list states
    delete_states(username, password, database)
