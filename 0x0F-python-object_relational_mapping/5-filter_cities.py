#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )
    registers = []
    cur = db.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %(state_name)s
        ORDER BY cities.id ASC""", {'state_name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            registers.append(col)
    print(", ".join(registers))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
