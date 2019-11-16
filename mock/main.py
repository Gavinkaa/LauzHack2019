from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    json_data = request.get_json()
    print(json_data["genomeUNK"])
    return True
