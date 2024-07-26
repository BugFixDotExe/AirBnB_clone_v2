#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index_route():
    """
    index (): returns the route for main
    Return: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    hbnb(): a function that maps to the /hbnb route
    Return: the string "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Handles the route /number/<text>.

    Args:
        n (int): The text obtained from the route.

    Returns:
        str: Display “n is a number” only if n is an integer
    """
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Handles the route to /number_template/<n>

    Args:
        n (int): The int or text obtained from route.

    Returns:
        A HTML: Disaply  display a HTML page only if n is an integer:

    Requirements:
        H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', number=n)


"""Checks if it's being imported or it's being run as a script """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
