#!/usr/bin/python3
""" that prints all City objects"""

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

# create an engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]),
    pool_pre_ping=True
)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

Base.metadata.create_all(engine)

stater_cities = session.query(State, City)\
                .filter(State.id == City.state_id).order_by(City.id).all()

for state, city in stater_cities:
    print("{}: ({}) {}".format(state.name, city.id, city.name))
