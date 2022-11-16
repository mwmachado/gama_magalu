from flask import Flask, redirect, url_for, request, render_template
import mysql.connector as sql

app = Flask(__name__)

# Função
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
contagem = "SELECT COUNT(*) FROM alunos;"
select_todos = "SELECT * FROM alunos;"
truncate = "TRUNCATE TABLE alunos;" #"DELETE FROM alunos;"

select_nome = "SELECT * FROM alunos WHERE nome like %s"
delete_nome = "DELETE FROM alunos WHERE nome like %s"
insert = "INSERT INTO alunos VALUES (%(nome)s,%(idade)s,%(filhos)s,%(estado)s,%(altura)s,%(formacao)s)"
update = '''
UPDATE alunos SET
    nome = %(nome)s,
    idade = %(idade)s,
    filhos = %(filhos)s,
    estado = %(estado)s,
    altura = %(altura)s,
    formacao = %(formacao)s
WHERE nome like %(nome)s  
'''

# index
@app.route('/')
def index():
    conexao, cursor = abrir_conexao()
    cursor.execute(contagem)
    resultado = cursor.fetchone()
    fechar_conexao(conexao)
    return {'registros': f'{resultado[0]} alunos'}

# read all
@app.route('/read')
def read():
    conexao, cursor = abrir_conexao(True)
    cursor.execute(select_todos)
    resultado = cursor.fetchall() #[(aluno1, ...), (aluno2, ...)]
    fechar_conexao(conexao)
    return resultado

# read por nome
@app.route('/read/<nome>')
def read_name(nome):
    conexao, cursor = abrir_conexao(True)
    cursor.execute(select_nome, [nome])
    resultado = cursor.fetchall()
    fechar_conexao(conexao)
    return resultado

# create
@app.route('/create')
#?nome=teste&idade=0&filhos=1&estado=AC&altura=0.07&formacao=Ensino+Superior
def create():
    aluno=request.args.to_dict() #{chave: valor, chave:valor,...}
    if aluno: # se tem argumento
        conexao, cursor = abrir_conexao()
        cursor.execute(insert, aluno)
        fechar_conexao(conexao)
        return aluno
    else: # se não tem argumento
        return redirect(url_for('static', filename='cadastro.html'))

# delete nome
@app.route('/delete/<nome>')
def delete_name(nome):
    conexao, cursor = abrir_conexao()
    cursor.execute(delete_nome, [nome])
    resultado = cursor.rowcount
    fechar_conexao(conexao)
    return {'message': f'{resultado} aluno(s) foram removido(s)!'}

# delete all
@app.route('/delete')
def delete_all():
    conexao, cursor = abrir_conexao()
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Todos os alunos foram apagados!'}

# update
@app.route('/update/<nome>')
#?nome=teste&idade=0&filhos=1&estado=AC&altura=0.07&formacao=Ensino+Superior
def update_name(nome):
    consulta = read_name(nome)
    print(consulta)
    if consulta: # existe nome no banco de dados
        aluno=request.args.to_dict() #{chave: valor, chave:valor,...}
        if aluno: # se tem argumento
            conexao, cursor = abrir_conexao()
            cursor.execute(update, aluno)
            fechar_conexao(conexao)
            return aluno
        else: # se não tem argumento
            return render_template('atualizacao.html', aluno=consulta[0])
    else: # não existe nome no banco de dados
        return {'error': 'Aluno não encontrado!'}


if __name__ == "__main__":
    app.run(debug=True)