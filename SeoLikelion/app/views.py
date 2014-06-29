from flask import render_template, Flask, jsonify, request
from app import app

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/_add_numbers')
def add_numbers():

    a = request.args.get('a')

    return jsonify(result=a)
