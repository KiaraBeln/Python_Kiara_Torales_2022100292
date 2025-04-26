
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello Wordl'
@app.route('/hola2', methods=['GET'])
def hola():
    return 'Hola 2'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port = 5000)
