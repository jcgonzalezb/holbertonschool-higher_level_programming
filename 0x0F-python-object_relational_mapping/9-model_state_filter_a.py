#!/usr/bin/python3
"""
Write a script that lists all State objects
that contain the letter 'a' from the database.
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

    myresult = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    for _row in myresult.all():
        print('{:d}: {:s}'.format(_row.id, _row.name))

    session.close()
