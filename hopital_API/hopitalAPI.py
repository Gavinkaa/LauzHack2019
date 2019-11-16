from flask import Flask, request
import flask
import sqlite3 as sq
from os import path
import requests

ip = "128.179.134.151:5000"
app = Flask(__name__)

def get_conn():
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = connect_db()
    return flask.g.sqlite_db


def execute_file(path, params):
    data = None
    with open(path, 'r') as file:
        data = file.read()
    conn = get_conn()
    c = conn.cursor()
    c.execute(data, params)
    return c.fetchall()


def connect_db():
    create_database = not path.exists("database.db")
    conn = sq.connect("database.db")
    if create_database:
        execute_file("setup.sql", [])
    return conn

def ask_sophia(genomes, pathogens):
    dataToSend = {"genomeUNK": genomes, "pathogens": pathogens}
    return requests.get(ip, json = dataToSend).json()

    

@app.route('/samples', methods=['POST'])
def add_samples():
    json = request.get_json()
    execute_file("create_hospital.sql", json)
    execute_file("create_room.sql", json)
    for room, genomes in json["rooms"].items():
        for gen in genomes:
            execute_file("create_genome.sql", {"seq":gen})
            execute_file("create_room_genome.sql", {"room": room, "genome":gen})
    get_conn().commit()
    result = ask_sophia(execute_file("all_genomes.sql",[]), execute_file("all_pathogens.sql",[]))
    return 'OK'

@app.route('/pathogens', methods=['POST'])
def add_pathogens():
    json = request.get_json
    for pathogen in json:
        execute_file("create_pathogen.sql", {"pathogen": pathogen})
    return 'OK'


app.run("0.0.0.0")
