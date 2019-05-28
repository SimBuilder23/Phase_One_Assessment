#!/usr/bin/env python3

import sqlite3

def create_database():
    connection = sqlite3.connect("state_parks.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists STATE_CITY_PARK(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            State VARCHAR,
            City VARCHAR
            Park VARCHAR
        );"""
    )

    cursor.close()
    connection.close()


create_database()

###     My Logic:
###     Keep State/City/Park in a single table, to maintain the relationship between City and Park
###     Sample queries:
###         1. All Parks in a State:
###             a. SELECT * from STATE_CITY_PARK where State = {state};
###         2. All Parks in a City:
###             a. SELECT * from STATE_CITY_PARK where City =  {city};
###         3. Which City, State is a Park located:
###             a. SELECT City, State from STATE_CITY_PARK where Park = {park};
