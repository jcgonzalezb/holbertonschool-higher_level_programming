#!/usr/bin/python3
"""
Write a script that prints the State object with the
name passed as argument from the database.
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
        State.name.like(argv[4]))

    if myresult.all():
        for _row in myresult.all():
            print('{:d}'.format(_row.id))
    else:
        print("Not found")

    session.close()
