from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/')
def index():
    return 'olá'

@app.route('/parametros')
#?nome=matheus
def parametros():
    argumentos = request.args.to_dict()
    return argumentos['nome'], 202

@app.route('/numero')
@app.route('/numero/<seed>')
def numero(seed=False):
    if seed:
        random.seed(seed)
    
    return {'numero': random.randint(0, 10)}, 201


if __name__ == "__main__":
    app.run(debug=True)