from flask import Flask, redirect, request, url_for
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('produtos.csv', index_col='produto')
carrinho = {} #{produto: [quantidade, valor]}
vendas = pd.read_csv('vendas.csv', index_col='produto')

#Inicial
@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

#Cadastro
@app.route('/cadastrar')
def cadastrar():
    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    valor = argumentos['valor']
    quantidade = argumentos['quantidade']
    
    df.loc[produto] = [valor, quantidade]
    print(df)
    return redirect(url_for('static', filename='cadastro.html'))

@app.route('/deletar/<produto>')
def deletar(produto):
    if produto in df.index:
        df.drop(produto, axis=0, inplace=True)
    else:
        print('produto não encontrado')
    
    print(df)
    return redirect(url_for('static', filename='cadastro.html'))

#Vendas
@app.route('/adicionar')
def adicionar():
    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    valor = argumentos['valor']
    quantidade = argumentos['quantidade']
    
    carrinho[produto] = [valor, quantidade]
    print(carrinho)
    return redirect(url_for('static', filename='vendas.html'))

@app.route('/carrinho')
def mostrar_carrinho():
    print(carrinho)
    return redirect(url_for('static', filename='carrinho.html'))

@app.route('/remover/<produto>')
def remover(produto):
    print(carrinho)
    print(carrinho.pop(produto, 'Produto não encontrado'))
    print(carrinho)
    return redirect(url_for('static', filename='carrinho.html'))

@app.route('/vender')
def vender():
    global vendas
    global carrinho

    for chave, valor in carrinho.items():
        if chave in vendas.index:
            vendas.loc[chave, 'quantidade'] = int(vendas.loc[chave, 'quantidade']) + int(valor[1])
        else:
            vendas.loc[chave] = valor
    
    carrinho = {}
    print(vendas)
    vendas.to_csv('vendas.csv')
    return redirect(url_for('static', filename='index.html'))

#Relatório
@app.route('/limpar')
def limpar():
    vendas = pd.DataFrame(columns=['produto','valor','quantidade'])
    vendas.to_csv('vendas.csv', index=False)
    return redirect(url_for('static', filename='relatorio.html'))

if __name__ == "__main__":
    app.run(debug=True)