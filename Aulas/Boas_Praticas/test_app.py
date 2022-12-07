import pytest
import requests
from app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_index_status_code(client):
    resultado = client.get('/')
    assert resultado.status_code == 200

def test_index_content(client):
    resultado = client.get('/')
    assert resultado.text == 'olá'

def test_parametros_content(client):
    resultado = client.get(f'/parametros', query_string={'nome': 'matheus'})
    assert resultado.text == 'matheus'

def test_parametros_type(client):
    resultado = client.get(f'/parametros', query_string={'nome': '3'})
    assert int(resultado.text)

def test_numero_random(client):
    seed = 0
    resultado = client.get(f'/numero/{seed}')
    assert {"numero": 5} == resultado.json
    assert resultado.status_code == 201

def test_google_com():
    response = requests.get('http://google.com')
    assert '<meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image">' in response.text
    

# resultado = requests.get('http://google.com')
# resultado = requests.get('http://127.0.0.1:5000')
# print(resultado.status_code == 200)
# print(resultado.text == 'olá')