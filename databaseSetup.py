#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('fitnessTracker.db')

print("Opened database successfully");

conn.execute('''DROP TABLE IF EXISTS WORKOUTRECORDS''')
#A record is this format: (id, workoutdate, workoutLength, workoutType, weight)

conn.execute('''CREATE TABLE WORKOUTRECORDS
    (ID INT PRIMARY KEY     NOT NULL,
    WORKOUTDATE            TEXT    NOT NULL,
    WORKOUTLENGTH   INT     NOT NULL,
    WORKOUTTYPE     TEXT    NOT NULL,
    WEIGHT          INT);''')

print("Table created successfully");

conn.close()
