#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa with their respective states."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the query to retrieve all cities and their states
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print each row in the specified format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
