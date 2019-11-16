from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def add_message():
    content = request.get_json()
    print(content)
    genome1 = content["genomeUNK"]
    print (genome1)
    return genome1
