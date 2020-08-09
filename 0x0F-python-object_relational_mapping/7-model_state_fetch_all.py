#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
    pool_pre_ping=True)

Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)
for instance in session.query(State).order_by(State.id).all():
    print("{}: {}".format(instance.id, instance.name))
session.close()
