#!pip install flask
from flask import Flask # importar a classe Flask
from flask import render_template
from flask import redirect
from flask import request
import pandas as pd

app = Flask(__name__) # criar o programa

# Criar a primeira rota
# rotas devem começar com /
@app.route('/')
def index():
    print("Hello print")  #é o que aparece no terminal
    return "Hello return" #é o que aparece no navegador

# Criar segunda rota
#@app.route('/outra_rota') # é possível ter duas rotas para o mesmo lugar
@app.route('/gama')
def gama():
    return 'sou uma nova rota'

@app.route('/com_barra/') # aceita tanto /com_barra/ quanto /com_barra
def com_barra():
    return "rota com barra"

@app.route('/sem_barra') # só aceita /sem_barra
def sem_barra():
    return "rota sem barra"

# o flask aceita receber parâmetros na url basta utilizar <>
@app.route('/hello/<name>') #hello/matheus
def hello(name):
    return f'Olá, {name}'
    #return f'Olá, {escape(name)} teste' #from markupsafe import escape

# rota caso o usuário utilize /hello/<name> errado
@app.route('/hello')
def hello_inicio():
    return 'a rota correta é /hello/<name>'


# lista para cadastramento de produtos
produtos = {} #{produto: valor}

# rota para listar produtos
@app.route('/listar')
def listar():
    return produtos

# rota para adicionar produtos, valores no dicionario
@app.route('/adicionar/<produto>/<valor>') # essa url substitui nosso input
def adicionar(produto, valor):
    #transformar valor (texto) para float
    #Insira um código para adicionar a chave produto com o valor no dicionario
    produtos[produto] = float(valor)
    return 'Produto adicionado'

# é possível acessar o arquivo de modo comum, site/static/formulario.html
# porém a fim de proteger o nome dos arquivos e pastas do projeto faça assim:

@app.route('/cadastro')
def cadastro():
    #cadastro?produto=nome_produto&valor=valor_produto
    argumentos = request.args.to_dict()
    #return argumentos
    return redirect('/static/parametros.html')

# rodar o app quando executar o programa app.py
if __name__ == "__main__":
    app.run(debug=True)