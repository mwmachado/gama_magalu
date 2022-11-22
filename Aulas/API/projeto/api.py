from flask import Flask, request
import mysql.connector as sql
app = Flask(__name__)

# Conexão com Banco de Dados
def abrir_conexao(dicionario=False):
    conexao = sql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="gamma"
    )
    cursor = conexao.cursor(dictionary=dicionario)
    return conexao, cursor

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

# Comandos SQL
colunas = ['filhos', 'formacao', 'altura', 'idade', 'estado', 'nome']
insert = '''
INSERT INTO alunos VALUES
(null, %(nome)s,%(idade)s,%(filhos)s,%(estado)s,%(altura)s,%(formacao)s);
'''
select_all = "SELECT * FROM alunos;"
select_by_id = "SELECT * FROM alunos WHERE id = %s;"
select_by_nome = "SELECT * FROM alunos WHERE nome = %s;"
delete_by_id = "DELETE FROM alunos WHERE id = %s;"
update = '''
UPDATE alunos SET
    nome = %(nome)s,
    idade = %(idade)s,
    filhos = %(filhos)s,
    estado = %(estado)s,
    altura = %(altura)s,
    formacao = %(formacao)s
WHERE id = %(id)s;
'''

# Erros
aluno_ausente = {'erro': "Aluno não encontrado"}, 404
coluna_ausente = {'erro': "Há coluna(s) faltando"}, 404
json_ausente = {'erro': 'Esperava receber um json no corpo da requisição'}, 400

# Rotas
## Create
@app.route('/cadastro', methods=['POST'])
def cadastrar():
    if request.get_json(silent=True):
        aluno = request.json
        conexao, cursor = abrir_conexao()
        cursor.execute(insert, aluno)
        fechar_conexao(conexao)
        return aluno, 201
    else:
        return json_ausente

## Read
@app.route('/consulta')
def consultar():
    conexao, cursor = abrir_conexao(True)
    cursor.execute(select_all)
    resultado = cursor.fetchall()
    fechar_conexao(conexao)
    return resultado, 200

@app.route('/consulta/<int:id>')
def consultar_id(id):
    conexao, cursor = abrir_conexao(True)
    cursor.execute(select_by_id, [id])
    resultado = cursor.fetchone()
    fechar_conexao(conexao)
    if resultado:
        return resultado, 200
    else:
        return aluno_ausente

@app.route('/consulta', methods=['POST'])
def consultar_nome():
    if request.get_json(silent=True):
        nome = request.json['nome']
        conexao, cursor = abrir_conexao(True)
        cursor.execute(select_by_nome, [nome])
        resultado = cursor.fetchall()
        fechar_conexao(conexao)
        if resultado:
            return {'resultado': resultado}, 200
        else:
            return aluno_ausente
    else:
        return json_ausente

## Update
@app.route('/atualizacao/<int:id>', methods=['PUT'])
def atualiza(id):
    resultado, status = consultar_id(id)
    if status == 200: #aluno está na base
        if request.get_json(silent=True):
            aluno = request.json
            if set(colunas) - set(aluno.keys()):
                return coluna_ausente
            conexao, cursor = abrir_conexao()
            aluno['id'] = id
            cursor.execute(update, aluno)
            fechar_conexao(conexao)
            return aluno, 200
        else:
            return json_ausente
    else:
        return aluno_ausente

## Delete
@app.route('/delecao/<int:id>', methods=['DELETE'])
def deleta(id):
    resultado, status = consultar_id(id)
    if status == 200: #aluno está na base
        conexao, cursor = abrir_conexao()
        cursor.execute(delete_by_id, [id])
        resultado = cursor.rowcount
        fechar_conexao(conexao)
        return {'message': f'{resultado} aluno(s) foram removido(s)!'}, 200
    else:
        return aluno_ausente

# Main
if __name__ == "__main__":
    app.run(debug=True, port=8000)