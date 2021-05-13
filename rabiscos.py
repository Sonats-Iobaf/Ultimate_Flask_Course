from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, Voce está na pagina inical!</h1>'.format(name)
    name = int(input('Digite seu nome: '))
    print(f'Hello{name}')

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'listkey': ['1, 2, 3']})

@app.route('/query')
def query():
    return '<h1>You are on the query page'
