from flask import Flask
from flask import request
from flask import jsonify
import random


app = Flask(__name__)

allName = ["VIH", "HUMAN", "PLANTES", "RHUMES", "VIRUS", "CANCER", "ANIMAL"] 

@app.route('/', methods=['GET'])
def add_message():
    args = request.get_json()
    ret = []
    for _ in args:
        depth = random.randint(0, 50)
        index = random.randint(0, len(allName)-1)
        name = allName[index]
        if name == "VIH" or name == "VIRUS" or name == "CANCER":
            danger = 1
        else:
            danger = 0
        temp = {"name": name, "dangerous": danger, "depth": depth}
        ret.append(temp)
    
    return {"species": ret}

app.run ("0.0.0.0")
