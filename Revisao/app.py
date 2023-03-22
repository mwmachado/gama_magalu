from flask import Flask, request

app = Flask(__name__)
numero = 0

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/soma', methods=["POST"])
def soma():
    json = request.get_json()
    total = json['x'] + json['y']
    return {"resultado": total}

@app.route('/contador', methods=["POST"])
def atualiza_contador():
    global numero
    json = request.get_json()
    numero = json['numero']
    return {'numero': numero}, 201

@app.route('/contador', methods=["GET"])
def get_contador():
    return {'numero': numero}, 200

@app.route('/contador/incrementa', methods=["PUT"])
def incrementa_contador():
    global numero
    numero = numero + 1
    return {'numero': numero}, 202

@app.route('/contador', methods=["DELETE"])
def zera_contador():
    global numero
    numero = 0
    return {'numero': numero}, 202
