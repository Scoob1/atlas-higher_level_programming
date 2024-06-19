#!/usr/bin/python3
""" List all State objects whos name match passed in argument in a database """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter_by(name=sys.argv[4]).first()

    if instance:
        print(instance.id)
    else:
        print("Not found")
