#!/usr/bin/python3
"""adds the State object Louisiana"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    louisiana = session.query(State).filter_by(name="Louisiana").first()
    print(louisiana.id)
    session.commit()
