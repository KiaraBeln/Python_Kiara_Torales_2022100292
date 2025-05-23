
from flask import Flask
from login import login

app = Flask(__name__)


###servicios rest

app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello mundo'


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port = 5001)
    app.run(debug = True)
   