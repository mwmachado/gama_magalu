from flask import render_template, redirect
from flask import Flask
from flask import request
import pandas as pd
app = Flask(__name__)
df = pd.read_json('produtos.json')

@app.route('/')
def listar_produtos():
    linhas = df.to_dict(orient='records')
    return render_template('lista_produtos.html', linhas=linhas)

@app.route('/adicionar')#/adicionar?produto=valor&preco=valor
def adicionar():
    global df
    argumentos = request.args.to_dict(False)
    '''
    pd.DataFrame({
        'produto':[valor],
        'preco':[valor],
    })
    '''
    print(argumentos)
    argumentos['id'] = [df['id'].max() + 1]
    print(argumentos)
    df = pd.concat([df, pd.DataFrame(argumentos)], ignore_index=True)
    df.to_json('produtos.json', orient='records')
    return redirect('/')


@app.route('/deletar/<id>')
def deletar(id):
    mask_id = df[df['id'] == int(id)].index
    df.drop(mask_id, axis=0, inplace=True)
    df.to_json('produtos.json', orient='records')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)