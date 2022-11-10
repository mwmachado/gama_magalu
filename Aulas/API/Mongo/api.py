from flask import Flask, request, redirect, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__)
conn = MongoClient('mongodb+srv://cluster0.rn9t8ag.mongodb.net/gama', username='gama', password='gama1234')
db = conn['magalu']

# Create
## Form
@app.route('/')
def home():
    return redirect(url_for('static', filename='cadastro.html'))

@app.route('/cadastro', methods=['GET'])
# ?nome=tomate&preco=10
def cadastro():
    produto = request.args.to_dict()
    db.produtos.insert_one(produto)
    # colocar um if para impedir cadastrar o mesmo produto 2 vezes
    del produto['_id']
    return produto

# Read

# Update
## Form

# Delete

if __name__ == '__main__':
    app.run(debug=True)