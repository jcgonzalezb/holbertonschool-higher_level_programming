#!/usr/bin/python3
"""
Write a script that prints the first State object from the database.
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

    first_object = session.query(State).order_by(State.id).first()

    if first_object:
        print('{:d}: {:s}'.format(first_object.id, first_object.name))
    else:
        print("Nothing")

    session.close()
