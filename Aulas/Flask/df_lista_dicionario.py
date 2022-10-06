from flask import Flask
from flask import request
import pandas as pd

app = Flask(__name__)
produtos_lista = []
precos = []
quantidades = []
produtos = {} # {produto: [valor, quantidade]}
'''
df = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')
'''
'''
iloc # posição 0,1,2,3,4,5
loc # index arroz, feijao
'''
df = pd.read_csv('produtos.csv', index_col='produto')
print(df)
@app.route('/')
def index():
    return "Hello!"

@app.route('/cadastro') # /cadastro?produto=valor_produto&valor=valor_preco&quantidade=valor_quantidade
def cadastro():
    argumentos = request.args.to_dict()
    '''
    {
        'produto': valor_produto,
        'preco': valor_preco,
        'quantidade': valor_quantidade,
    }
    '''
    produto = argumentos['produto']
    preco = argumentos['preco']
    quantidade = argumentos['quantidade']
    #listas
    produtos_lista.append(produto)
    precos.append(preco)
    quantidades.append(quantidade)
    #dicionario
    produtos[produto] = [preco, quantidade]
    #dataframe
    df.loc[produto] = [preco, quantidade]
    df.to_csv('produtos.csv')
    return 'Produtos foram cadastrados'

@app.route('/lista')
def lista():
    return [produtos_lista, precos, quantidades] #bruno

@app.route('/dicionario')
def dicionario():
    return produtos #fernando

@app.route('/dataframe')
def dataframe():
    print(df)
    return 'verifique no terminal'

if __name__ == "__main__":
    app.run(debug=True)