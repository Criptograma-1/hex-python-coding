#!/usr/bin/python3
"""
script that adds the State object 'Louisiana'
to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State, City)\
        .filter(State.id == City.state_id)\
        .order_by(City.id)

    for state, city in states_cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
