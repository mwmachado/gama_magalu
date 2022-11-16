#pip install mysql-connector-python
import mysql.connector as sql
conexao = sql.connect(
    host="127.0.0.1",
    user="root",
    password="gama1234",
    database="filmes"
)
cursor = conexao.cursor(dictionary=True)

cursor.execute("SELECT * FROM usuarios;")
resultado = cursor.fetchall()
print(resultado)

conexao.close()