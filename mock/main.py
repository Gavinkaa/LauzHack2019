from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    args = request.args
    a = args["genomeUNK"]
    b = args["genome1"]
    return str(a == b)
