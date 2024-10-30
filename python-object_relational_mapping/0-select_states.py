#!/usr/bin/python3
import sys           # Import sys to handle command-line arguments
import MySQLdb       # Import MySQLdb to connect to the MySQL database

# This block ensures the code only runs when the script is executed directly
if __name__ == "__main__":
    # Get command-line arguments: MySQL username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",    # Database server (localhost for local server)
        user=username,       # MySQL username
        passwd=password,     # MySQL password
        db=database,         # Database name
        port=3306            # MySQL port (default is 3306)
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to get all rows from "states" table, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results from the executed query
    rows = cursor.fetchall()

    # Loop through the results and print each row
    for row in rows:
        print(row)  # Each row is displayed as a tuple, e.g., (1, 'California')

    # Close the cursor to free resources
    cursor.close()

    # Close the database connection
    db.close()
