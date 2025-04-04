#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa using MySQLdb."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SELECT query to fetch all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print each row in the result set
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
