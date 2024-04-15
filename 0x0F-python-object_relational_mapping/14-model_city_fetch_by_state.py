#!/usr/bin/python3
"""script that lists all Cities by State objects
from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_cities(username, password, database):
    """function listing all states"""
    # Create engine
    engine = create_engine(f"mysql://{username}:{password}\
                            @localhost:3306/{database}")

    # Create session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and sort states by id
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        state_name = session.query(State.name).filter(
                State.id == city.state_id).first()
        print(f"{state_name[0]} : ({city.id}) {city.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to list states
    list_cities(username, password, database)
