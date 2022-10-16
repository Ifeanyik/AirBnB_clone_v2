#!/usr/bin/python3
'''this scripts starts a Flask web application'''


from flask import Flask

app = Flask(__name__)


@app.route('/')
def display():
    '''this function returns a string
    for any url starting with /'''
    return "Hello HBNB!"

if __name__ == "main":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
else:
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
