#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    index (): returns the route for main
    Return: "Hello HBNB!"
    """
    return "Hello HBNB!"


"""Checks if it's being imported or it's being run as a script """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
