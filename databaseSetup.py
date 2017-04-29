#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('fitnessTracker.db')

print("Opened database successfully");

cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS WORKOUTRECORDS''')
#A record is this format: (id, workoutdate, workoutLength, workoutType, weight)

cur.execute('''CREATE TABLE WORKOUTRECORDS
    (ID TEXT PRIMARY KEY     NOT NULL,
    WORKOUTDATE            TEXT    NOT NULL,
    WORKOUTLENGTH   TEXT     NOT NULL,
    WORKOUTTYPE     TEXT    NOT NULL,
    WEIGHT          TEXT);''')

conn.commit()
conn.close()
print("Table created successfully");

conn.close()
