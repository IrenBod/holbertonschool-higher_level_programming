#!/usr/bin/python3
"""Deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command-line arguments for connecting to the database
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connection string to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with a name containing the letter 'a'
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to apply the deletions
    session.commit()

    # Close the session
    session.close()
