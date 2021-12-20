#!/usr/bin/python3
"""
Write a script that takes in the name of a state as
an argument and lists all cities of that state,
using the database.
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

    myquery = """SELECT cities.name \
            FROM cities, states \
            WHERE states.id = cities.state_id \
            AND states.name = %s ORDER BY cities.id ASC"""

    mycursor.execute(myquery, (argv[4],))

    myresult = mycursor.fetchall()

    string = []
    for values in myresult:
        for i in values:
            string.append(i)

    print(*string, sep=', ')
    mycursor.close()
    db.close()
