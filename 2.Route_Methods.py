from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

'''Roots are going to be an essential component to your app because thats how people
 re going to access the diferent areas of your app or the different parts of your API.'''
@app.route('/home', methods=['POST', 'GET'])
def home():
    return '<h1>You are on the home page!</h1>'

@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'listkey' : ['1, 2, 3']})

'''Dictionaries and lists a dictionary maps to an object in jason and lists maps to an array'''


if __name__ == '__main__':
    app.run(debug=True)

'''Just know that by defaut the only method that is alloowed is GETS 
and if you want to alolow diferent methods than you have to use the 
methods parameter and pass a list of the accepted methods for that particular route.'''



