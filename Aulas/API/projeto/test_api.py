import pytest
import mysql.connector as sql
from api import app

@pytest.fixture()
def client():
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == 'olá'

def test_cadastro(client):
    example = {
        'nome':'teste',
        'idade': 0,
        'filhos': 0,
        'estado': 'AA',
        'altura': 2,
        'formacao': ''
    }
    response = client.post('/cadastro', json=example)
    assert response.status_code == 201
    assert response.json == example

def test_consulta(client):
    response = client.get('/consulta')
    assert response.status_code == 200

def test_consulta_nome(client):
    response = client.post('/consulta', json={'nome':'teste'})
    assert response.status_code == 200
    assert 'resultado' in response.json.keys()

def test_delecao(client):
    response = client.post('/consulta', json={'nome':'teste'})
    id = response.json['resultado'][0]['id']
    response = client.delete(f'/delecao/{id}')
    assert response.status_code == 200
    assert response.json == {'message': f'1 aluno(s) foram removido(s)!'}