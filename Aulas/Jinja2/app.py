from flask import Flask, url_for, redirect, render_template, escape
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return 'home'

@app.route("/estatico")
def estatico():
    return redirect(url_for('static', filename="index.html"))

@app.route("/template/<nome>")
def template(nome):
    return render_template("index.html", usuario=nome)

@app.route("/decisao/<int:numero>")
def decisao(numero):
    return render_template("decisao.html", opcao=numero)

@app.route('/alunos')
def alunos():
    df = pd.read_csv('alunos.csv')
    alunos = df['alunos'].to_list()
    return render_template('lista.html', lista = alunos)

@app.route('/notas')
def notas():
    df = pd.read_csv('alunos_completo.csv')
    #alunos = df['aluno'].to_list()
    #notas = df['nota'].to_list()
    return render_template('lista_completa.html', dataframe = df)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/tabela')
def tabela():
    df = pd.read_csv('alunos_completo.csv')
    tabela = df.to_html()
    return render_template('tabela.html', tabela=tabela)

@app.route('/arquivo/<path:script>')
def injection(script):
    return escape(script)

if __name__ == "__main__":
    app.run(debug=True)