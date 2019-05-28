#!/usr/bin/env python3

import sqlite3

def create_database():
    connection = sqlite3.connect("doctors_patients.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE if not exists DOCTOR_PATIENT(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Doctor VARCHAR,
            Patient VARCHAR
        );"""
    )

    cursor.close()
    connection.close()



create_database()


### My Logic:
### Keep a single table where each record is a combination of Doctor and Patient
### Sample Queries:
###     1. All Patients associated with a particular Doctor:
###         a. SELECT Patient from DOCTOR_PATIENT where Doctor = {particular_doctor};
###     2. All Doctors associated with a particular Patient:
###         a. SELECT Doctor from DOCTOR_PATIENT where Patient = {particular_patient};
