from flask import Flask, request,jsonify, make_response,url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def index():
    print(request)
    print(request.method)
    print(request.args.to_dict())
    # print(request.json)
    if request.data:
        print(request.json)
    return {"message":"olá"}, 201

@app.route('/delete', methods=['delete'])
def delete():
    return 'deletado'


if __name__ == "__main__":
    app.run(debug=True, port=8000)