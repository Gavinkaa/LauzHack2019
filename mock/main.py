from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def add_message():
    content = request.get_json()
    unk = content["genomeUNK"]
    genomes = content["genomes"]

    truesIndexes = []

    for i, genome in enumerate(genomes):
        if unk == genome:
            truesIndexes.append(i)

    return jsonify(truesIndexes)
