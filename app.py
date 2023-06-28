import json
from flask import Flask, jsonify, request

app = Flask(__name__)

with open("destiny.json") as destiny_file:
    destiny = json.load(destiny_file)

with open("origin.json") as origin_file:
    origin = json.load(origin_file)

with open("send.json") as send_file:
    send = json.load(send_file)

# Listar todos os grupos
@app.route('/groups', methods=['GET'])
def getGroups():
    return jsonify(origin, destiny)

# Listar todas as configurações de envio
@app.route('/senders', methods=['GET'])
def getSenders():
    return jsonify(send)

# Buscar grupo de destino por id
@app.route('/groups/destiny/<int:id>', methods=['GET'])
def getGroupDestinyById(id):
    for group in destiny:
        if group.get('group_id') == id:
            return jsonify(group)

# Buscar grupo de origem por id
@app.route('/groups/origin/<int:id>', methods=['GET'])
def getGroupOriginById(id):
    for group in origin:
        if group.get('group_id') == id:
            return jsonify(group)

@app.route('/groups/<int:id>', methods=['PUT'])
def updateGroups(id):
    group_data = request.get_json()
    return request.get_json()
    

@app.route('/groups/origin', methods=['GET'])
def getGroupsOrigin():
    return jsonify(groups)

@app.route('/groups/destiny', methods=['GET'])
def getGroupsDestiny():
    return jsonify(groups)


app.run(port=8080, debug=True, host='localhost')