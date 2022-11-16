import pandas as pd
import mysql.connector as mysql
import sqlite3 as sqlite
from pymongo import MongoClient
from pprint import pprint

# # Conexão
con_sqlite = sqlite.connect('pandas.bd')
# con_sqlite.row_factory = sqlite.Row
con_mysql = mysql.connect(
    username='root',
    password='gama1234',
    host='127.0.0.1',
    database='pandas'
)
con_mongo = MongoClient(
    'mongodb+srv://cluster0.rn9t8ag.mongodb.net/pandas',
    username='gama',
    password='gama1234'
)

# # Cursor
cur_sqlite = con_sqlite.cursor()
cur_mysql = con_mysql.cursor(dictionary=True)
cur_mongo = con_mongo['pandas']


# Object Relational Mapper

# tabela -> linha -> objeto

# sql -> sqlalchemy -> python
# python -> sqlalchemy -> sql

# SQL Alchemy
# pip install sqlalchemy
from sqlalchemy import create_engine
eng_sqlite = create_engine("sqlite:///pandas.bd")
eng_mysql = create_engine("mysql+mysqlconnector://root:gama1234@127.0.0.1/pandas")


# Ler o arquivo CSV
# df = pd.read_csv('alunos.csv')
# print(df.head())

#CR Mongo
## Create
# pprint(df.to_dict('records'))
# cur_mongo.alunos.insert_many(df.to_dict('records'))

## Read
# resultado = list(cur_mongo.alunos.find({}))
# df_mongo = pd.DataFrame(resultado).set_index('_id')
# print(df_mongo)

#CR SQLite
## Create
# df.to_sql('alunos', eng_sqlite)

## Read
# print(cur_sqlite.execute('select * from alunos;').fetchall())
# df_sqlite = pd.read_sql_table('alunos', eng_sqlite)
# print(df_sqlite.head())

# CR MySQL
## Create
# df.to_sql('alunos', eng_mysql, index=False, if_exists='replace')

## Read
# df_mysql = pd.read_sql_query('select * from alunos;', eng_mysql)
# print(df_mysql.head())