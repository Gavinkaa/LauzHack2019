from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def add_message():
    return 'OK'