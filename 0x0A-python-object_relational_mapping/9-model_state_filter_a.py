#!/usr/bin/python3
"""list all State objects that contain the letter a from a database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    a = '%a%'

    states = session.query(State).filter(State.name.like(a)).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
