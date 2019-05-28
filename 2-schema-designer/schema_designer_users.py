#!/usr/bin/env python3

import sqlite3

def create_database():
    ### creates table of regular users
    connection = sqlite3.connect("users.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists USERS(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Username VARCHAR,
            Name VARCHAR,
            Password TEXT,
            Email TEXT
        );"""
    )


    ### creates table of ADMIN USER... to keep ADMIN USER's data separate from regular users data  (i.e. partition of data)

    cursor.execute(
        """CREATE TABLE if not exists ADMIN(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Username VARCHAR,
            Name VARCHAR,
            Password TEXT,
            Email TEXT
        );"""
    )


    ### creates table of phone numbers for both users and admin

    cursor.execute(
        """CREATE TABLE if not exists PHONES(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Username VARCHAR,
            Phone TEXT
        );"""
    )

    cursor.close()
    connection.close()


create_database()


### My Logic:
### Keep separate user tables for regular users and the admin, but can still use a single table for phone numbers (of all users)
### Sample Queries:
### 1. Want phone numbers for particular user:
###     a. SELECT Phone from PHONES where Username = {some_username};
### 2. Want the user's name to go with the above?
###     a. SELECT users.name, phones.phone FROM USERS INNER JOIN PHONES ON USERS.username = PHONES.username;
