#!/usr/bin/env python3

import sqlite3

def create_database():
    connection = sqlite3.connect("doctors_patients.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists DOCTOR_PATIENTS(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Doctor VARCHAR,
            Patient VARCHAR
        );"""
    )

    cursor.close()
    connection.close()


    connection = sqlite3.connect("doctors_patients.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists PATIENT_DOCTORS(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Patient VARCHAR,
            Doctor VARCHAR
        );"""
    )

    cursor.close()
    connection.close()    

create_database()