#!/usr/bin/python3
''' First time with Flask '''
from flask import Flask
app = Flask(__name__)

app.url_map.strict_slashes = False
app.run(host='0.0.0.0', port=5000)

@app.route('/')
def hello_world():
    return "Hello HBNB!"
