#pip install pymongo
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

def consulta_mongo(db, colecao, consulta, retorno=False):
    cursor = db[colecao].find(consulta)
    resultado = list(cursor)
    pprint(resultado)
    if retorno:
        return resultado

def print_secao(secao):
    print()
    print('='*len(secao))
    print(secao)
    print('='*len(secao))
    print()
    
# Create Read Update Delete

# # Conexão
print_secao('Conexão ao Banco MongoDB')
cliente = MongoClient('mongodb+srv://cluster0.rn9t8ag.mongodb.net/gama', username='gama', password='gama1234')
db = cliente['gama']

# READ
## Consulta
print_secao('Consulta')
resultado = consulta_mongo(db, 'alunos', {}, retorno=True)

## Pandas
df = pd.DataFrame(resultado).set_index('_id')
print(df)

## Arquivo
df.to_json('mongo.json', orient='records')

#UPDATE
print_secao('Update')

# UPDATE alunos SET
#     Idade = Idade-10
# WHERE Idade > 40
consulta_mongo(db, 'alunos', {'Idade': {'$gt':40}}, retorno=True)

db.alunos.update_many(
    {'Idade': {'$gt':40}},
    {'$set':
        {"Idade":30}
    }
)

resultado = consulta_mongo(db, 'alunos', {'Nome': 'Anderson'}, retorno=True)
db.alunos.update_one(
    {'Nome': 'Anderson'},
    {'$set':
        {'Idade': resultado[0]['Idade'] - 10}
    } 
)

consulta_mongo(db, 'alunos', {'Nome': 'Anderson'})

#DELETE
print_secao('Delete')
consulta_mongo(db, 'alunos', {'Nome': 'Anderson'}, retorno=True)
consulta_mongo(db, 'alunos', {'Idade': {'$gte':30}}, retorno=True)
db.alunos.delete_one({'Nome': 'Anderson'})
db.alunos.delete_many({'Idade': {'$gte':30}})

print_secao('Depois do Delete')
consulta_mongo(db, 'alunos', {'Idade': {'$gte':30}}, retorno=True)
consulta_mongo(db, 'alunos', {'Nome': 'Anderson'}, retorno=True)

# #INSERT
print_secao('INSERT')
db.drop_collection('alunos')
db.alunos.insert_one({"Nome": "Matheus"})
df = pd.read_json('mongo.json')
pprint(df.to_dict('records'))
db.alunos.insert_many(df.to_dict('records'))