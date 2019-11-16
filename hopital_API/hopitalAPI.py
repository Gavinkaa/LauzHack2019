from flask import Flask
from flask import request
import sqlite3 as sq 
from os import path 



def executeFile(pathToFile, cursor, params):
    data = None
    with open(pathToFile, 'r') as file:
        data = file.read().replace('\n', '').split(";")
    for line in data:
        cursor.execute(line, params)
    return cursor.fetchall()

create_database = not path.exists("database.db")
conn = sq.connect("database.db") 
cursor = conn.cursor()   
if create_database:
    executeFile("setup.sql", cursor, [])
    
app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_message():
    conn = sq.connect("database.db")
    cursor = conn.cursor()
    args = request.get_json()
    hopital = args["hopital"]
    roomsWithGenome = args["room"]
    #Put hopital in the table
    #a = executeFile("insert.sql", conn.cursor(), hopital)
    print(hopital)
    with open("insert.sql", 'r') as file:
        data = file.read().replace('\n', '').split(";")
    for line in data:
        print(line)
        cursor.execute(line, [hopital])
        conn.commit()
    return 'OK'

app.run("0.0.0.0")