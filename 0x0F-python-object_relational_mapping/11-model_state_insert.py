#!/usr/bin/python3
"""adds the State object Louisiana"""

from model_state import Base, State
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
new_state = State(name="Santa ana")
session.add(new_state)
session.commit()
