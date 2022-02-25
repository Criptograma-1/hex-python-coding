#!/usr/bin/python3

"""Script to starts a Flask web Application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def C(text):
    return ("C " + text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
