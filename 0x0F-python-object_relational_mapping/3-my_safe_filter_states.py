#!/usr/bin/env python3
""" script that lists all states with a name starting with N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = %(state_name)s ORDER BY id ASC",
            {
                'state_name': argv[4]
            }
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
