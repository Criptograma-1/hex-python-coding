#!/usr/bin/python3
"""script lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access DB and get the cities"""

    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    with db.cursor() as c:
        c.execute("""
            SELECT
                cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(arg)s
            ORDER BY
                cities.id ASC
        """, {'arg': argv[4]})

        rows = c.fetchall()

    if rows is not None:
        print(", ".join(city[0] for city in rows))
