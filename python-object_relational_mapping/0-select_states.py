#!/usr/bin/python3
"""This module is all about maping object,
and connecting a database.
"""
import sys
import MYSQLdb


if __name__ == "__main__":
db = MYSQLdb.connect( 
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')
cursor=db.cursor()
cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
states = cursor.fetchall()
for state in states:
    print(state)
