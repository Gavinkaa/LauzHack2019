from flask import Flask
from flask import request
from flask import jsonify
import random
import json

class TrieNode(object):

    def __init__(self, char, depth, specie, danger):
        self.char = char
        self.children = []
        self.word_finished = False
        self.depth = depth
        self.specie = specie
        self.danger = danger


def add(root, word, specie, danger):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char, node.depth+1, specie, danger)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix):
<<<<<<< HEAD

    parentsSpecie = None
    parentsDang = False
    node = root
    size = 1
    if not root.children:
        return 0, 0, False
    for char in prefix:
        size += 1
        char_not_found = True
        for child in node.children:
            if child.char == char:
                if node.specie != None:
                    parentsSpecie = node.specie
                parentsDang = node.danger
                char_not_found = False
                node = child
                break
        if char_not_found:
            return node.depth, parentsSpecie, parentsDang
    return node.depth, parentsSpecie, parentsDang


#POPULATE TRIE 
with open("species.json", 'r') as file:
    data = json.load(file)
root = TrieNode('*', 0, "Living", False)
for name, data in data.items():
    add(root, data[0], name, data[1])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def analyze():
    args = request.get_json()
    res = []
    for sequence in args:
        depth, parent, dangerous = find_prefix(root, sequence)
        if dangerous:
            res.append({'name':parent, 'dangerous': 1, 'depth':depth})
        else:
            res.append({'name':parent, 'dangerous': 0, 'depth':depth})
    return {"species": res}

@app.route('/samples', methods=['POST'])
def retrieve_samples():
    args = request.get_json()
    for k,v in args.items():
        add(root, v[0], k, v[1])
=======

    parentsSpecie = None
    parentsDang = False
    node = root
    size = 1
    if not root.children:
        return 0, 0, False
    for char in prefix:
        size += 1
        char_not_found = True
        for child in node.children:
            if child.char == char:
                if node.specie != None:
                    print("changing to : ", node.specie)
                    parentsSpecie = node.specie
                parentsDang = node.danger
                char_not_found = False
                node = child
                break
        if char_not_found:
            return node.depth, parentsSpecie, parentsDang
    return node.depth, parentsSpecie, parentsDang


#POPULATE TRIE 
with open("species.json", 'r') as file:
    data = json.load(file)
root = TrieNode('*', 0, "Living", False)
for name, data in data.items():
    add(root, data[0], name, data[1])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def add_message():
    args = request.get_json()
    res = []
    for sequence in args:
        depth, parent, dangerous = find_prefix(root, sequence)
        if dangerous:
            res.append({'name':parent, 'dangerous': 1, 'depth':depth})
        else:
            res.append({'name':parent, 'dangerous': 0, 'depth':depth})
    return {"species": res}
>>>>>>> master

app.run ("0.0.0.0")