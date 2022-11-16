# Biblioteca e Conexão
import sqlite3 as sql
conexao = sql.connect('projeto.db')

# Cursor e Executando Comandos
cursor = conexao.cursor()
# ## Criar tabela
cursor.execute('''DROP TABLE IF EXISTS alunos;''')
cursor.execute('''
CREATE TABLE alunos(
    nome text,
    idade int,
    filhos int,
    estado text,
    altura real,
    formacao text
);
''')

# Lista todas as tabelas do banco de dados
cursor.execute('''
    SELECT name
    FROM sqlite_master
    WHERE type='table';
''')

# cursor.fetchone -> 1 registro no formato de tupla
# cursor.fetchmany(n) -> n registros em formato de tupla dentro de uma lista
# cursor.fetchall() -> todos registros em formato de tupla dentro de uma lista

print(cursor.fetchall())

## Inserir dados
cursor.execute('''
INSERT INTO alunos VALUES
    ('Anderson',40,0,'SP',1.90,'Superior Incompleto (ADS)'),
    ('Ettore Mitsueda',29,2,'SP',1.72,'Ensino Médio Completo'),
    ('Bruna',28,0,'MG',1.62,'Superior completo'),
    ('clara',19,0,'RJ',1.63,'superior incompleto (ADS)'),
    ('João Paulo',27,0,'DF',1.50,'Superior completo'),
    ('Fernando A',32,1,'SP',1.74,'Mestrado completo/Doutorado incompleto'),
    ('José Vitor',24,0,'PB',1.78,'superior incompleto'),
    ('Raissa',32,2,'GO',1.68,'Superior'),
    ('George',38,0,'CE',1.80,'Superior'),
    ('Bruno Coelho',30,0,'SP',1.70,'Superior '),
    ('Fernando Oliveira',41,0,'SP',1.79,'Superior'),
    ('Edson',26,0,'PR',1.80,'Superior Incompleto'),
    ('Eron',32,1,'SP',1.76,'Ensino Médio Completo'),
    ('Fernando',23,0,'RN',1.70,'Ensino Médio'),
    ('Wagner',30,0,'CE',1.73,'Superior Completo'),
    ('Gabrielle',25,0,'RJ',1.56,'Superior Completo'),
    ('Larissa',28,0,'RJ',1.74,'Ensino Superior Completo'),
    ('Câmara',58,1,'RJ',1.80,'Superior Completo'),
    ('William Ferrari',40,3,'SP',1.73,'Superior incompleto'),
    ('Erick',26,0,'SP',1.70,'Ensino Superior Completo'),
    ('lucas',26,0,'SP',1.70,'superior'),
    ('Willian Caetano',37,1,'pa',1.75,'superior'),
    ('Divino',24,0,'SP',1.69,'Superior'),
    ('Natalia',25,0,'SS',1.59,'Ensino Médio Completo'),
    ('julia',30,0,'pa',1.59,'superior completo'),
    (' Gabriel Silva',27,0,'SP',1.80,'superior incompleto'),
    ('Bruno Fernandes',25,0,'SC',1.90,'Superior incompleto'),
    ('Josivaldo',35,8,'SP',1.80,'Ensino medio Completo'),
    ('BRUNO LIMA',32,0,'pr',1.80,'Pós graduado'),
    ('Sandro Santos Marra',38,0,'DF',1.83,'Ensino Superior Inc'),
    ('Gabriel Queiroz',23,0,'MG',1.78,'Superior Completo')
;''')
# cursor.execute("select count(*) from alunos;")
# print(cursor.fetchall())
# conexao.rollback() # Descarta as alterações
conexao.commit() # Salva as alterações no banco de dados
cursor.execute("select count(*) from alunos;")
print(cursor.fetchall())

# ## Consultar dados
# cursor.execute('''
# SELECT *
# FROM alunos
# WHERE idade > 40
# ;''')

# print(cursor.fetchone())

# ## Inserindo múltiplas linhas
# data = [
#     ('Matheus',23,0,'MG',1.78,'Superior Completo'),
#     ('Ana',23,0,'MG',1.78,'Superior Completo')
# ]

# # Evita o SQLInjection
# cursor.executemany('''
# INSERT INTO alunos VALUES
# (?,?,?,?,?,?)
# ''', data)

# '''
# INSERT INTO alunos VALUES
# ('Matheus',23,0,'MG',1.78,'Superior Completo')
# '''
# '''
# INSERT INTO alunos VALUES
# ('Ana',23,0,'MG',1.78,'Superior Completo')
# '''

# data = [
#     {
#         'nome':'Matheus',
#         'idade':23,
#         'filhos':0,
#         'estado':'MG',
#         'altura':1.78,
#         'formacao':'Superior Completo'
#     },
#     {
#         'nome':'Ana',
#         'idade':23,
#         'filhos':0,
#         'estado':'MG',
#         'altura':1.78,
#         'formacao':'Superior Completo'
#     }
# ]
# cursor.executemany(f'''
# INSERT INTO alunos VALUES
# (:nome,:idade,:filhos,:estado,:altura,:formacao)
# ''', data)
# '''
# INSERT INTO alunos VALUES
# ('Matheus',23,0,'MG',1.78,'Superior Completo')
# '''
# '''
# INSERT INTO alunos VALUES
# ('Ana',23,0,'MG',1.78,'Superior Completo')
# '''

# cursor.commit()

# Fechar Conexão
conexao.close()