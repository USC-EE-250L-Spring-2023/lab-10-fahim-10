from flask import Flask, request, jsonify
from sys import stdout
from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.
@app.route('/process1', methods=["POST"])
def computeProcess1():
    res = request.get_json(force=True)
    res = res['data']
    res = process1(res)
    res = jsonify(res)
    return res

@app.route('/process2', methods=["POST"])
def computeProcess2():
    res = request.get_json(force=True)
    res = res['data']
    res = process2(res)
    res = jsonify(res)
    return res