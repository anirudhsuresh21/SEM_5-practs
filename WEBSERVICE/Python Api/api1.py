import flask
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

dictn = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

@app.route("/",methods = ['GET'])
def hello():
    return jsonify(message="Hello World")

@app.route('/convert', methods=['POST'])
def convert_number():
    result = ""
    num1 = request.json['num1']
    for i in num1:
        result += dictn[i]
        result += " "

    return jsonify({'result': result})


app.run(debug=True)