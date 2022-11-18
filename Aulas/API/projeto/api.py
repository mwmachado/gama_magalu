from flask import Flask, request
import mysql.connector as sql
app = Flask(__name__)

# Conexão com Banco de Dados
def abrir_conexao(dicionario=False):
    conexao = sql.connect(
        host="127.0.0.1",
        user="root",
        password="gama1234",
        database="gama"
    )
    cursor = conexao.cursor(dictionary=dicionario)
    return conexao, cursor

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

# Comandos SQL
insert = '''
INSERT INTO alunos VALUES
(null, %(nome)s,%(idade)s,%(filhos)s,%(estado)s,%(altura)s,%(formacao)s)
;
'''
select_all = "SELECT * FROM alunos;"
select_by_id = "SELECT * FROM alunos WHERE id = %s;"

# Rotas
@app.route('/cadastro', methods=['POST'])
def cadastrar():
    if request.get_json(silent=True):
        aluno = request.json
        conexao, cursor = abrir_conexao()
        cursor.execute(insert, aluno)
        fechar_conexao(conexao)
        return aluno, 201
    else:
        return {'erro': 'Esperava receber um json no corpo da requisição'}, 400

@app.route('/consulta')
def consultar():
    conexao, cursor = abrir_conexao(True)
    cursor.execute(select_all)
    resultado = cursor.fetchall()
    fechar_conexao(conexao)
    return resultado

@app.route('/consulta/<int:id>')
def consultar_id(id):
    conexao, cursor = abrir_conexao(True)
    cursor.execute(select_by_id, [id])
    resultado = cursor.fetchone()
    fechar_conexao(conexao)
    if resultado:
        return resultado
    else:
        return {'erro': "Aluno não encontrado"}, 404

'''
   1. Retornar apenas um item pelo nome [POST] {"nome": "nome do item"}
   1. Atualizar um item pelo id [PUT] {"nome": "novo_nome", ...}
   1. Deletar um item pelo id [DELETE <id>]
'''
if __name__ == "__main__":
    app.run(debug=True, port=8000)