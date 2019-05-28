#!/usr/bin/env python3

import sqlite3

def create_database():
    connection = sqlite3.connect("state_parks.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists STATE_CITIES(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            State VARCHAR,
            City VARCHAR
        );"""
    )

    cursor.close()
    connection.close()


    connection = sqlite3.connect("state_parks.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists STATE_PARKS(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            State VARCHAR,
            Park VARCHAR
        );"""
    )

    cursor.close()
    connection.close()

create_database()

### My Design Logic:
### 1) KISS: keep separate tables for each combination of datasets--
###     a. one table of State+City (works for any number of States), and,
###     b. one table of State+Parks (again, works)
###
