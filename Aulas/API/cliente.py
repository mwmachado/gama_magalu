import requests
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    pedido = requests.get('http://127.0.0.1:5001/')
    if pedido.status_code == 200:
        print(pedido.json())
    return 'olá do cliente'

if __name__ == "__main__":
    app.run(debug=True, port=5000)