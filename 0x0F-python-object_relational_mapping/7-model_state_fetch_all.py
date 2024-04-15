#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states(username, password, database):
    """function listing all states"""
    # Create engine
    engine = create_engine(f"mysql://{username}:{password}\
                            @localhost:3306/{database}")

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and sort states by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to list states
    list_states(username, password, database)
