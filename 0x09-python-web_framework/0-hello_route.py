#!/usr/bin/python3

"""Script to starts a Flask web Application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
