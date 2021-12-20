#!/usr/bin/python3
"""
Write a script that prints all City objects from the database
"""


from sys import argv
from sqlalchemy import create_engine, asc
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username = argv[1]
    passwrd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwrd, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    myquery = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).order_by(asc(City.id))

    for q in myquery:
        print("{:s}: ({:d}) {:s}".format(q[0], q[1], q[2]))

    session.close()
