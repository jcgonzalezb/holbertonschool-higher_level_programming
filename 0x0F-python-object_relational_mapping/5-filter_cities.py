#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all
values in the states table of the database where name matches the argument.
Write one that is safe from MySQL injections.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities, states \
                    WHERE states.id = cities.state_id \
                    ORDER BY cities.id ASC;")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mycursor.close()
    db.close()
