#!/usr/bin/ python3
import MySQLdb
import sys

# This script connects to a MySQL database and
# safely retrieves entries from the states table.
# Usage: ./3-my_safe_filter_states.py <username>
# <password> <database> <state_name>

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL database on localhost at port 3306
    db = MySQLdb.connect(host="localhost", 
                         port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Define the query with a parameterized placeholder to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Display each row as a tuple
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
