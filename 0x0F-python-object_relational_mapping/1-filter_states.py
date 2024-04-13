#!/usr/bin/python3
""" a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database):
    """function list all states with a name starting with N"""
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create cursor
    cursor = db.cursor()

    # Execute query to select all states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call function to list states
    list_states(username, password, database)
