from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)
#conn = MongoClient('mongodb+srv://username:password@cluster0.rn9t8ag.mongodb.net/magalu'
conn = MongoClient(
    'mongodb+srv://cluster0.rn9t8ag.mongodb.net/magalu',
    username='gama',
    password='gama1234'
)
db = conn['magalu']

# Create
@app.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))

@app.route('/cadastrar/', methods=['GET'])
# ?nome=tomate&preco=10
def cadastrar():
    produto = request.args.to_dict() #{'nome': 'tomate', 'preco':10}
    print(produto)
    if not produto: #{}
        return redirect(url_for('static', filename='cadastrar.html'))
    else: #{'nome': 'tomate', 'preco':10}
        query = db.produtos.find_one({'nome': produto['nome']})
        # find => Cursor => list(Cursor) [{}, {}]
        # find_one => {}
        if query: #tomate está no banco
            return {'error': 'Produto já cadastrado!'}
        else: # tomate não está no banco
            db.produtos.insert_one(produto)
            del produto['_id']
            return produto

# Read
@app.route('/consultar/')
def consultar():
    cursor = db.produtos.find({}, {'_id':False})
    produtos = list(cursor)
    return produtos

@app.route('/consultar/<nome>')
def consultar_nome(nome):
    produto = db.produtos.find_one({'nome': nome}, {'_id':False})
    print(produto)
    if produto: #tomate está no banco
        return produto
    else: # tomate não está no banco
        return {'error': 'Produto não encontrado!'}

# Update
#?nome=tomate&preco=10
@app.route('/atualizar/')
def atualizar():
    produto = request.args.to_dict() #{'nome': 'tomate', 'preco':10}
    print(produto)
    if not produto: #{}
        produtos = consultar()
        print(produtos)
        return render_template('atualizar.html', produtos=produtos)
    else: #{'nome': 'tomate', 'preco':10}
        db.produtos.update_one(
            {'nome': produto['nome']},
            {'$set':
                {'preco': produto['preco']}
            }
        )
        return produto

# Delete
@app.route('/deletar/<nome>')
def deletar_nome(nome):
    produto = db.produtos.find_one({'nome': nome}, {'_id':False})
    print(produto)
    if produto: #tomate está no banco
        db.produtos.delete_one({'nome': nome})
        return {'message': 'Produto deletado com sucesso!'}
    else: # tomate não está no banco
        return {'error': 'Produto não encontrado!'}

@app.route('/deletar/')
def deletar():
    db.produtos.drop()
    return {'message': 'Banco de dados apagado!'}

if __name__ == '__main__':
    app.run(debug=True)