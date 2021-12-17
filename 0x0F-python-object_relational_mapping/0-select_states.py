#!/usr/bin/python3
"""
Write a script that lists all values inside table states from the database.
Should take 3 arguments: mysql username, mysql password and database name.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id ASC;")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mycursor.close()
    db.close()
