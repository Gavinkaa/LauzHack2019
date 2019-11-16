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

conn = sq.connect("database.db")
cursor = conn.cursor()
if not path.exists("database.db"):    
    executeFile("setup.sql", cursor, [])
    
app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_message():
    args = request.get_json()
    hopital = args["hopital"]
    roomsWithGenome = args["room"]
    #Put hopital in the table
    #a = executeFile("insert.sql", conn.cursor(), hopital)
    with open("insert.sql", 'r') as file:
        data = file.read().replace('\n', '').split(";")
    for line in data:
        cursor.execute(line, hopital)
    return cursor.fetchone()

app.run("0.0.0.0")