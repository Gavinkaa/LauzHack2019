from flask import Flask, request
import flask
import sqlite3 as sq
from os import path


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


app = Flask(__name__)


@app.route('/samples', methods=['POST'])
def add_sample():
    execute_file("create_hospital.sql", request.get_json())
    get_conn().commit()
    return 'OK'


app.run("0.0.0.0")
