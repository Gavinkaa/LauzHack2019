from flask import Flask, request
import flask
import sqlite3 as sq
from os import path
import requests

toConnect = "http://128.179.134.151:5000"
app = Flask(__name__)


def get_conn():
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = connect_db()
    return flask.g.sqlite_db


def execute_setup():
    data = None
    conn = get_conn()
    c = conn.cursor()
    with open("sql/setup.sql", 'r') as file:
        data = file.read().split(";")
    for line in data[:len(data)-1]:
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


def connect_db():
    create_database = not path.exists("database.db")
    conn = sq.connect("database.db")
    if create_database:
        execute_setup()
    return conn


def ask_sophia(genomes, pathogens):
    genomes = [item[0] for item in genomes]
    pathogens = [item[0] for item in pathogens]
    dataToSend = {"genomeUNK": genomes, "pathogens": pathogens}
    return requests.get(toConnect, json=dataToSend).json()


def update_matches():
    result = ask_sophia(execute_file("sql/all_genomes.sql", []),
                        execute_file("sql/all_pathogens.sql", []))
    genomes = execute_file("sql/all_genomes.sql", [])
    genomes = [str(item[0]) for item in genomes]
    allPathogens = execute_file("sql/all_pathogens.sql", [])
    allPathogens = [str(item[0]) for item in allPathogens]
    for res, gen in zip(result, genomes):
        for indexPathogen in res:
            pathogen = allPathogens[indexPathogen]
            execute_file("sql/create_match.sql",
                         {"genome": gen, "pathogen": pathogen})
    get_conn().commit()


def is_pathogen(gen):
    return len(execute_file("sql/pathogen_check.sql", [gen])) != 0


@app.route('/samples', methods=['POST'])
def add_samples():
    json = request.get_json()
    execute_file("sql/create_hospital.sql", json)
    for room, genomes in json["rooms"].items():
        execute_file("sql/create_room.sql",
                     {"room": room, "hospital": json["hospital"]})
        for gen in genomes:
            execute_file("sql/create_genome.sql", {"seq": gen})
        get_conn().commit()
        for gen in genomes:
            execute_file("sql/create_room_genome.sql",
                         {"room": room, "genome": gen})
    get_conn().commit()
    update_matches()
    newPathogens = []
    for room, genomes in json["rooms"].items():
        for gen in genomes:
            if is_pathogen(gen):
                newPathogens.append({"pathogen": gen, "room": room})
    ret = {"hospital": json["hospital"], "samples": newPathogens}
    print(ret)
    requests.post("http://128.179.186.221:1234/alert", json=ret)
    return 'OK add sample'


@app.route('/pathogens', methods=['POST'])
def add_pathogens():
    json = request.get_json()
    for pathogen in json:
        execute_file("sql/create_pathogen.sql", {"pathogen": pathogen})
    get_conn().commit()
    update_matches()
    return 'ok add pathogens'


app.run("0.0.0.0")
