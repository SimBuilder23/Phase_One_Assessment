#!/usr/bin/env python3

import sqlite3

def create_database():
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

    cursor.close()
    connection.close()


    connection = sqlite3.connect("users.db", check_same_thread=False)
    cursor = connection.cursor()

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