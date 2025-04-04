#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (uppercase N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server running on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    # Execute query with case-sensitive filter using BINARY
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print all rows that match the condition
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
