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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb(): a function that maps to the /hbnb route
    Return: the string "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    c(): a function that handles the route /c/<text>
    it takes in extra args from the user.

    Args:
        text (str): The text got from route is padded to,
    the function c as an argunmnet, for further
    processing.

    Return:
        str: The input string with the C attached
    exampl: C is fun
    """
    text = text.replace("_",  " ")
    return (f"C {text}")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Handles the route /python/<text>.

    Args:
        text (str): The text obtained from the route, with underscores
                    replaced by spaces.
                    If no text is provided, the default value is 'is cool'.

    Returns:
        str: The input string with "Python" prefixed.
             Example: 'Python is fun' if the route was /python/is_fun.

    Requirement:
        The default value of text is “is cool”.
    """
    text = text.replace("_", " ")
    return f"Python {text}"


"""Checks if it's being imported or it's being run as a script """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
