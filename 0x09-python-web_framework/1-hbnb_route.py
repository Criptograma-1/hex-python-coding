#!/usr/bin/python

"""Script to starts a Flask web Application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'
