import json
from flask import Flask, jsonify, request

app = Flask(__name__)

with open("destiny.json") as destiny_file:
    destiny = json.load(destiny_file)

with open("origin.json") as origin_file:
    origin = json.load(origin_file)

with open("send.json") as send_file:
    send = json.load(send_file)

# Listar todas as configurações de envio
@app.route('/senders', methods=['GET'])
def getSenders():
    return jsonify(send)

# Inserir configuração de envio
@app.route('/senders', methods=["POST"])
def insertSender():
    new_send = request.get_json()
    send.append(new_send)
    with open("send.json", "w") as send_file:
        json.dump(send, send_file, indent = 2)
    return jsonify(send)

# Deletar configuração de envio
@app.route('/senders/<int:id>', methods=["DELETE"])
def deleteSender(id):
    for index, config in enumerate(send):
        if config.get("send_id") == id:
            del send[index]
            with open("send.json", "w") as send_file:
                json.dump(send, send_file, indent=2)
            return jsonify(send)

# Listar todos os grupos
@app.route('/groups', methods=['GET'])
def getGroups():
    return jsonify(origin, destiny)

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

# Editar grupo de destino por id
@app.route('/groups/destiny/<int:id>', methods=['PUT'])
def updateGroupDestiny(id):
    group_data = request.get_json()
    for group in destiny:
        if group.get('group_id') == id:
            group.update(group_data)
            with open("destiny.json", "w") as destiny_file:
                json.dump(destiny, destiny_file, indent=2)
            return jsonify(group)

# Editar grupo de origem por id
@app.route('/groups/origin/<int:id>', methods=['PUT'])
def updateGroupOrigin(id):
    group_data = request.get_json()
    for group in origin:
        if group.get('group_id') == id:
            group.update(group_data)
            with open("origin.json", "w") as origin_file:
                json.dump(origin, origin_file, indent=2)
            return jsonify(group)

# Inserir grupo de origem
@app.route('/groups/destiny', methods=["POST"])
def insertGroupDestiny():
    new_group = request.get_json()
    destiny.append(new_group)
    with open("destiny.json", "w") as destiny_file:
        json.dump(destiny, destiny_file, indent=2)
    return jsonify(destiny)

# Inserir grupo de origem
@app.route('/groups/origin', methods=["POST"])
def insertGroupOrigin():
    new_group = request.get_json()
    origin.append(new_group)
    with open("origin.json", "w") as origin_file:
        json.dump(origin, origin_file, indent=2)
    return jsonify(origin)

# Deletar grupo de destino
@app.route('/groups/destiny/<int:id>', methods=["DELETE"])
def deleteGroupDestiny(id):
    for index, group in enumerate(destiny):
        if group.get("group_id") == id:
            del destiny[index]
            with open("destiny.json", "w") as destiny_file:
                json.dump(destiny, destiny_file, indent=2)
            return jsonify(destiny)

# Deletar grupo de origem
@app.route('/groups/origin/<int:id>', methods=["DELETE"])
def deleteGroupOrigin(id):
    for index, group in enumerate(origin):
        if group.get("group_id") == id:
            del origin[index]
            with open("origin.json", "w") as origin_file:
                json.dump(origin, origin_file, indent=2)
            return jsonify(origin)

app.run(port=8080, debug=True, host='localhost')