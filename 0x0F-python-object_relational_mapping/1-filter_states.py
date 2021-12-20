#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N
(upper N) from the database
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

    mycursor.execute("SELECT * FROM states WHERE \
                    name LIKE 'N%' ORDER BY id ASC;")

    myresult = mycursor.fetchall()

    for x in myresult:
        if x[1][0] == 'N':
            print(x)

    mycursor.close()
    db.close()
