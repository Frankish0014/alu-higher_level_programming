#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Collect arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    # Create the query with .format() as instructed
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute and fetch results
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    # Cleanup
    cursor.close()
    db.close()
