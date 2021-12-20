#!/usr/bin/python3
"""
Write a script that deletes all State objects
with a name containing the letter a from the database
"""


from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    username = argv[1]
    passwrd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwrd, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    x = session.query(State).filter(State.name.like('%a%'))

    for _row in x.all():
        session.delete(_row)

    session.commit()

    session.close()
