#!/usr/bin/python3
"""This script lists all cities of a given state
    from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Define the query with a parameterized
    # placeholder to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    # Execute the query with the state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the results as a comma-separated list
    print(", ".join(row[0] for row in rows))

    # Close the cursor and database connection
    cursor.close()
    db.close()
