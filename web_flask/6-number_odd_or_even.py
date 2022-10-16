#!/usr/bin/python3
'''this scripts starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
def display():
    '''this function returns a string
    for any url starting with /'''
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    '''returns a string for any url
    starting with /hbnb'''
    return "HBNB"


@app.route("/c/<text>")
def c_is_what(text):
    '''returns a string for urls matching /c/'''
    new_text = ""
    for i in text:
        if i == "_":
            new_text += " "
        else:
            new_text += i
    return "C {}".format(new_text)


@app.route("/python/<text>")
@app.route("/python/")
@app.route("/python")
def weird(text="is cool"):
    '''returns a string for urls matching /python/<variable_text>'''
    if text == "is cool":
        return "Python {}".format(text)
    else:
        new_text = ""
        for i in text:
            if i != "_":
                new_text += i
            else:
                new_text += i
        return "Python {}".format(new_text)


@app.route("/number/<int:n>")
def catch_numbers(n):
    '''Check if <n> is a number'''
    return "%d is a number" % n


@app.route("/number_template/<int:n>")
def display_html(n):
    """Returns an html page only if n is an integer"""
    from flask import render_template
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def display_html_odd_or_even(n):
    """Returns a html page stating if n is odd or even"""
    from flask import render_template
    even_or_odd = ""
    if n % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template("6-number_odd_or_even.html", n=n, even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
