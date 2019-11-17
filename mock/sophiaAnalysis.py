from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def add_message():
    content = request.get_json()
    unks = content["genomeUNK"]
    genomes = content["pathogens"]

    truesIndexes = []

    for j, unk in enumerate(unks):
        temp = []
        for i, genome in enumerate(genomes):
            if unk == genome:
                temp.append(i)

        truesIndexes.append(temp)

    return jsonify(truesIndexes)

app.run ("0.0.0.0", port=5001)
