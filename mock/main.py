from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def add_message():
    content = request.get_json()
    unks = content["genomeUNK"]
    genomes = content["genomes"]

    truesIndexes = []

    for j, unk in enumerate(unks):
        temp = []
        for i, genome in enumerate(genomes):
            if unk == genome:
                temp.append(i)

        truesIndexes.append(temp)

    return jsonify(truesIndexes)
