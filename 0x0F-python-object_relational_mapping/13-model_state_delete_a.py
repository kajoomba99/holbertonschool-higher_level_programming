#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""

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
    session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session=False)
    session.commit()
    session.close()
