#!/usr/bin/python3
"""Thos project is about going to bedtime,
and mapping."""
import sys
import MYSQLdb


if __name__ = "__main__":
    db = MYSQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host='localhost'),
    c = db.cursor()
    c.execute('SELECT * FROM cities ORDER BY cities.id ASC;')
    cities = c.fetchall()
    for city in cities:
        print(city)
