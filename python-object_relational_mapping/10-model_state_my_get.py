#!/usr/bin/python3
'''
prints the State object with the name passed as argument
#!/usr/bin/python3

A script that prints the State object ID from the database `hbtn_0e_6_usa`
with the name passed as an argument. If the state does not exist, it prints "Not found".

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username: The username for the MySQL server.
    mysql_password: The password for the MySQL server.
    database_name: The name of the MySQL database to connect to.
    state_name: The name of the State to search for.

Example:
    ./script_name.py root root123 hbtn_0e_6_usa Texas

Dependencies:
    - SQLAlchemy: Install using `pip install SQLAlchemy`
    - MySQLdb: Install using `pip install mysqlclient`
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    state = session.query(State).filter(State.name == argv[4]).first()
    print('Not found' if not state else state.id)
    session.close()
