#!/usr/bin/python3
"""Жodule that displays all values matched the argument in the `states`."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to find states matching the specified name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query)

    # Fetch and print all results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
