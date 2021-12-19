#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to the database
"""


from sys import argv
from sqlalchemy import create_engine, desc
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

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    myresult = session.query(State).order_by(desc(State.id)).first()

    print('{:d}'.format(myresult.id))

    session.close()
