#!/usr/bin/python3
""" a script that lists all states with a name starting with given text
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_cities(username, password, database, srch_term):
    """function list all cities with a name 'srch_term'"""
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create cursor
    cursor = db.cursor()

    # SQL query with parameterized query
    query = "SELECT * FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id"

    # Execute query with parameter
    cursor.execute(query, (srch_term + '%',))

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
    username, password = sys.argv[1], sys.argv[2]
    database, srch_term = sys.argv[3], sys.argv[4]

    # Call function to list cities
    list_cities(username, password, database, srch_term)
