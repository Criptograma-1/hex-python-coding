#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access DB and get states"""
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = c.fetchall()
    for row in rows:
        print(row)
