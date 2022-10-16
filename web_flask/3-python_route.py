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


@app.route("/python/(<text>)")
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
            elif i == "(" or i == ")":
                continue
            else:
                new_text += i
        return "Python {}".format(new_text)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
