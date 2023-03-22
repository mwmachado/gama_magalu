from flask import Flask
import sqlite3 as sql

app = Flask(__name__)

def create_database():
    if app.config['TESTING']: #por padrão TESTING=False
        con = sql.connect('test.db')
    else:
        con = sql.connect('production.db')
    con.close()

@app.route('/')
def index():
    create_database()
    return 'ola'

if __name__ == "__main__":
    app.run(debug=True)