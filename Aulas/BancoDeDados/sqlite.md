# SQLite
- SQLite possui tipo flexível, que significa que especificar o tipo de dado de cada coluna é opcional.
- Para confirmar uma transacao é necessário rodar o comando commit.
- O comando commit salva as alteracoes no banco de dados.
- Lembre-se sempre de fechar a conexão ao final do programa, caso contrário ela pode ficar aberta consumindo recursos.

# SQLite e Python
- Umas das bibliotecas Python utilizadas para manipular SQLite é a PySQLite.
- PySQLite é parte das bibliotecas padrões do python.
- A biblioteca cria automaticamente um banco de dados em arquivos caso não exista. Caso exista, ela abre uma conexão.

# Objetos SQLite
- A biblioteca possui 3 objetos principais: Connection (conexão), Cursor (cursor), e Row (linha).
- Conection: representa o banco de dados em si, é utilizada para criação de cursores, e controle de transações.
- Cursor: utilizado para executar comandos no banco de dados e receber os resultados.
- Row: representa uma linha da tabela e suas colunas.

# Tipos de dados
- SQLite nativamente suporta os seguintes tipos de dados:
    - NULL
    - INTEGER
    - REAL
    - TEXT
    - BLOB
- tipos de dados: https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types

# Referencia
- https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types
- https://www.sqlitetutorial.net/sqlite-python/

# Prática

```python
# Biblioteca e Conection
import sqlite3 as sql
conexao = sql.connect('projeto.db')

# Cursor e Executando comandos
## Criando tabela
resultado = cursor.execute(create_table)
## Inserindo dados
cursor.execute(insert)
## Consultando dados
resultado = cursor.execute(select)
resultado.fetchone()
## Confirmando alterações
conexao.commit()
#conexao.rollback()

## Inserindo múltiplas linhas
data = [
    (valor1, valor2),
    (valor3, valor4),
    (valor5, valor6)
]
cursor.executemany('INSERT INTO nome_tabela VALUES(?,?,?)', data)
# ou
# cursor.executemany('INSERT INTO nome_tabela VALUES(:chave1,:chave2,:chave3)', {chave1:valor1, chave2:valor2, chave3: valor3})
'''Sempre utilize ? no lugar de f-strings para evitar SQL Injection
'''
resultado.fetchall()
conexao.commit()

# Demonstrando SQL Injection

# Imprimindo resultado 
resultado = cursor.execute(select)
for linha in resultado:
    print(linha)

# Rows e Acessando colunas
resultado = cursor.execute(select)
linha = resultado.fetchone()
linha.keys()
linha[0]
linha[1]
linha['coluna1']
linha['coluna2']

# Apagando tabela
cursor.execute(drop)
conexao.commit()
cursor.execute(select)

# Encerrando a conexão
conexao.close()
```

# SQL
```sql
CREATE TABLE nome_tabela(coluna1, coluna2, ...);

INSERT INTO nome_tabela VALUES (valor1, valor2, ...);

SELECT coluna FROM nome_tabela;

INSERT INTO nome_tabela
VALUES
    (valor1, valor2, ...),
    (valor1, valor2, ...),
    (valor1, valor2, ...),
    ...
;

DROP TABLE nome_tabela;
```
