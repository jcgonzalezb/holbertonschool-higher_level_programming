#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all
values in the states table of the database where name matches the argument.
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

    mycursor.execute("SELECT * FROM states ORDER BY id ASC;")

    myresult = mycursor.fetchall()

    for i, j in myresult:
        if j == argv[4]:
            print("({}, '{}')". format(i, j))

    mycursor.close()
    db.close()
