#
# Lucas Eren
# EtimoDb.py
# 
# Creates the database for the assignment
#

import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('etimoDatabase.db')

# Create a cursor (makes it possible to connect to db)
cur = connection.cursor()

# Create a table
cur.execute("DROP TABLE IF EXISTS etimo")   #Restart 

cur.execute('''CREATE TABLE etimo (
                email TEXT PRIMARY KEY NOT NULL,
                firstname TEXT NOT NULL, 
                lastname TEXT NOT NULL)''')

cur.execute("INSERT INTO etimo VALUES ('abc@hotmail.com', 'Kalle', 'Johansson')")


rows = cur.execute("SELECT * FROM etimo").fetchall()
for r in rows: 
    print(r)

# Commit the changes and close the connection
connection.commit()
connection.close()