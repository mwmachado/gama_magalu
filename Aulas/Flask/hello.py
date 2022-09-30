from flask import Flask, url_for, render_template, request
from markupsafe import escape
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route("/<path:name>")
def hello_name(name):
    #return f"Hello, {name}"
    return f"Hello, {escape(name)}!"

@app.route("/caminho/")
def caminho():
    return "posso ser acessado sem a barra no final"

@app.route("/caminho2")
def caminho2():
    return "não posso ser acessado com a barra no final"

@app.route("/url_for")
def url():
    #return url_for('caminho')
    #return url_for('caminho', variavel='valor')
    #return url_for('hello_name', name="matheus")
    return url_for('hello_name', name="matheus", variavel='valor')

@app.route('/render_template')
def render():
    return render_template('hello.html')

@app.route('/render_template/<name>')
def render_name(name):
    return render_template('hello_name.html', name=name)

@app.route('/ganhou_ou_perdeu/<resultado>')
def ganhou_perdeu(resultado):
    return render_template('ganhou_perdeu.html', resultado=resultado)

@app.route('/ganhadores/<ganhadores>')
def ganhadores(ganhadores=[]):
    ganhadores = ganhadores.split(',')
    return render_template('ganhadores.html', ganhadores=ganhadores)

@app.route('/rotas')
def rotas():
    return render_template('rotas.html')

# @app.route('/form')
@app.route('/request')
def parametros():
    param = pd.Series(request.args.to_dict())
    param.to_csv('parametros.csv', header=False)
    return render_template('request.html', argumentos=request.args)