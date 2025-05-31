from flask import Flask, request, jsonify
from cliente import cliente

app = Flask(__name__)
###servicios rest
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello mundo'

if __name__ == '__main__':
    app.run(host='localhost', debug = True, port = 5003)