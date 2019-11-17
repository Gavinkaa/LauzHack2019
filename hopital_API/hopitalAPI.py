from flask import Flask, request
import flask
import sqlite3 as sq
from os import path
import requests

MOCK_API = "http://128.179.134.151:5000"
WS_API = "http://128.179.186.221:1234"
ALERT_DEPTH = 4
app = Flask(__name__)


def connect_db():
    create_database = not path.exists("database.db")
    conn = sq.connect("database.db")
    if create_database:
        execute_setup()
    return conn


def get_conn():
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = connect_db()
    return flask.g.sqlite_db


def commit():
    get_conn().commit()


def execute_setup():
    conn = get_conn()
    c = conn.cursor()
    data = None
    with open("sql/setup.sql", 'r') as file:
        data = file.read().split(";")
    for line in data[:-1]:
        c.execute(line)
    conn.commit()


def execute_file(path, params):
    data = None
    with open(path, 'r') as file:
        data = file.read()
    conn = get_conn()
    c = conn.cursor()
    c.execute(data, params)
    return c.fetchall()


def ask_sophia(genomes):
    # requests.get(MOCK_API, json=dataToSend).json()
    return [
        {"name": "HIV", "dangerous": 1, "depth": 22},
        {"name": "Human", "dangerous": 0, "depth": 16}
    ][:len(genomes)]


def update_matches():
    genomes = [str(item[0])
               for item in execute_file("sql/all_genomes.sql", [])]
    matches = ask_sophia(genomes)
    for m in matches:
        execute_file("sql/create_species.sql",
                     {"species": m["name"], "dangerous": m["dangerous"], "depth": m["depth"]})
    commit()
    for (g, m) in zip(genomes, matches):
        execute_file("sql/create_match.sql", {"gen": g, "species": m["name"]})
    commit()


def is_dangerous(gen):
    return len(execute_file("sql/is_dangerous.sql", {"gen": gen, "depth": ALERT_DEPTH})) != 0


@app.route('/samples', methods=['POST'])
def add_samples():
    json = request.get_json()
    execute_file("sql/create_hospital.sql", json)
    for room, genomes in json["rooms"].items():
        execute_file("sql/create_room.sql",
                     {"room": room, "hospital": json["hospital"]})
        for gen in genomes:
            execute_file("sql/create_genome.sql", {"seq": gen})
        commit()
        for gen in genomes:
            execute_file("sql/create_room_genome.sql",
                         {"room": room, "genome": gen})
    commit()
    update_matches()
    newPathogens = []
    for room, genomes in json["rooms"].items():
        for gen in genomes:
            if is_dangerous(gen):
                newPathogens.append({"pathogen": gen, "room": room})
    ret = {"hospital": json["hospital"], "samples": newPathogens}
    requests.post(WS_API + "/alert", json=ret)
    return "OK add sample"


app.run("0.0.0.0")
