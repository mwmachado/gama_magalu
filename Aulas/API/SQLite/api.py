from flask import Flask, redirect, url_for, request, render_template
import sqlite3 as sql

app = Flask(__name__)
banco = 'gama.bd'

# Função
def abrir_conexao(banco):
    conexao = sql.connect(banco)
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

# Comandos SQL
contagem = "SELECT COUNT(*) FROM alunos;"
select_todos = "SELECT * FROM alunos;"
truncate = "DELETE FROM alunos;" #"TRUNCATE TABLE alunos;"

select_nome = "SELECT * FROM alunos WHERE nome like ?"
delete_nome = "DELETE FROM alunos WHERE nome like ?"
insert = "INSERT INTO alunos VALUES (:nome,:idade,:filhos,:estado,:altura,:formacao)"
update = '''
UPDATE alunos SET
    nome = :nome,
    idade = :idade,
    filhos = :filhos,
    estado = :estado,
    altura = :altura,
    formacao = :formacao
WHERE nome like :nome  
'''

# index
@app.route('/')
def index():
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(contagem).fetchone()
    fechar_conexao(conexao)
    return {'registros': f'{resultado[0]} alunos'}

# read all
@app.route('/read')
def read():
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(select_todos).fetchall() #[(aluno1, ...), (aluno2, ...)]
    fechar_conexao(conexao)
    return resultado

# read por nome
@app.route('/read/<nome>')
def read_name(nome):
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(select_nome, [nome]).fetchall()
    fechar_conexao(conexao)
    return resultado

# create
@app.route('/create')
#?nome=teste&idade=0&filhos=1&estado=AC&altura=0.07&formacao=Ensino+Superior
def create():
    aluno=request.args.to_dict() #{chave: valor, chave:valor,...}
    if aluno: # se tem argumento
        conexao, cursor = abrir_conexao(banco)
        cursor.execute(insert, aluno)
        fechar_conexao(conexao)
        return aluno
    else: # se não tem argumento
        return redirect(url_for('static', filename='cadastro.html'))

# delete nome
@app.route('/delete/<nome>')
def delete_name(nome):
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(delete_nome, [nome]).rowcount
    fechar_conexao(conexao)
    return {'message': f'{resultado} aluno(s) foram removido(s)!'}

# delete all
@app.route('/delete')
def delete_all():
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Todos os alunos foram apagados!'}

# update
@app.route('/update/<nome>')
#?nome=teste&idade=0&filhos=1&estado=AC&altura=0.07&formacao=Ensino+Superior
def update_name(nome):
    consulta = read_name(nome)
    if consulta: # existe nome no banco de dados
        aluno=request.args.to_dict() #{chave: valor, chave:valor,...}
        if aluno: # se tem argumento
            conexao, cursor = abrir_conexao(banco)
            cursor.execute(update, aluno)
            fechar_conexao(conexao)
            return aluno
        else: # se não tem argumento
            return render_template('atualizacao.html', aluno=consulta[0])
    else: # não existe nome no banco de dados
        return {'error': 'Aluno não encontrado!'}


if __name__ == "__main__":
    app.run(debug=True)