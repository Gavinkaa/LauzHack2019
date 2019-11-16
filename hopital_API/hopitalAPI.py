from flask import Flask
from flask import request
import sqlite3 as sq 
from os import path 


if not path.exists("database.db"):
    conn = sq.connect("database.db")
    cursor = conn.cursor()
    with open("setup.sql", 'r') as file:
        data = file.read().replace('\n', '').split(';')
    for elem in data:
        cursor.execute(elem)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_message():
    args = request.get_json()
    hopital = args["hopital"]
    roomsWithGenome = args["room"]
    for room in roomsWithGenome.key():
        for genome in room:
            
    




    return 'OK'