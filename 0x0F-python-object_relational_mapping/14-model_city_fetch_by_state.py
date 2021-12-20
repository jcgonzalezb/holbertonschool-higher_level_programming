#!/usr/bin/python3
"""
Write a script that prints all City objects from the database
"""


import sqlalchemy as db
from sqlalchemy.engine.url import URL
from sys import argv
from sqlalchemy import create_engine, asc
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":

    username = argv[1]
    passwrd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwrd, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(City.state_id.__eq__(State.id)).order_by(asc(City.id))

    for _row in query.all():
        print(_row.name, _row.cities.id, _row.name)

    session.close()