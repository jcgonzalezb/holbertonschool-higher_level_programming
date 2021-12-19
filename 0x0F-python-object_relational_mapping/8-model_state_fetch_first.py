#!/usr/bin/python3
"""
Write a script that prints the first State object from the database.
"""


import sqlalchemy as db
from sqlalchemy.engine.url import URL
from sys import argv
from sqlalchemy import create_engine, asc
from model_state import Base, State


if __name__ == "__main__":

    engine = db.create_engine(
        db.engine.url.URL.create(
            drivername='mysql',
            username=argv[1],
            password=argv[2],
            host='localhost',
            port=3306,
            database=argv[3]))

    meta_data = db.MetaData(bind=engine)
    db.MetaData.reflect(meta_data)

    STATES = meta_data.tables['states']

    myquery = db.select([STATES]).where(STATES.c.id == 1)

    myresult = engine.execute(myquery).fetchall()

    for i, j in myresult:
        print("{}: {}". format(i, j))
