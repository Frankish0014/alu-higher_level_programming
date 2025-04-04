#!/usr/bin/python3
"""
Safe from SQL injection:
Displays all values in the states table where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Take arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    # Close connections
    cursor.close()
    db.close()
