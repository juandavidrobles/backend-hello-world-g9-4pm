from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
  return 'Hello world'

@app.route('/hola')
def hello2():
  return {'message': 'Buenas tardes desde el servidor!'}

@app.route('/bye')
def hello3():
  return 'Bye folks!'