#!/usr/bin/env python3

# Code copied from link in lab manual

import sqlite3

#connect to database file
dbconnect = sqlite3.connect("mydatabase_ex1.db");

#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;

#now we create a cursor to work with db
cursor = dbconnect.cursor();

#execute insert statement
#cursor.execute('''insert into temps values ('2013-10-09', '10:57', "kitchen", 2.1)''');
dbconnect.commit();

#execute simple select statement
cursor.execute('SELECT * FROM temps');

#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );

#ex4, part1
cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
#ex4, part2
cursor.execute('SELECT * FROM sensors WHERE type="door"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);



#close the connection
dbconnect.close();


