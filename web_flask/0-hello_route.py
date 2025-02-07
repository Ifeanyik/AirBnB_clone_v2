#!/usr/bin/python3
'''this scripts starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    '''this function returns a string
    or any url starting with /'''
    return "Hello HBNB!"


@app.route('/airbnb-onepage/', strict_slashes=False)
def serve_onepage():
    return "Hello ALX Africa!!!"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
