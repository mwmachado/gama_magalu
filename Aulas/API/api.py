from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def api():
    if request.method == "GET":
        print(request.args.to_dict())
    elif request.method == "POST":
        print(request.form.to_dict())
        #if request.data:
        if request.get_json(silent=True): # se foi enviado json no corpo da requisição
            print(request.json)
        else: # se não foi enviado json no corpo da requisição
            return {"error": "esperava receber um json"}, 400
    else:
        return {'error': 'foi utilizado um método diferente de get e post'}, 405
    return {"message": f"O método utilizado foi {request.method}"}

@app.route('/form')
def form():
    #print(request.form.to_dict())
    return redirect(url_for('static', filename='cadastro.html'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)