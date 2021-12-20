#!/usr/bin/python3
"""
Write a script that lists all State objects from the database.
"""


from sys import argv
from sqlalchemy import create_engine, asc
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

    myquery = session.query(State).order_by(asc(State.id))

    for q in myquery.all():
        print('{:d}: {:s}'.format(q.id, q.name))

    session.close()
