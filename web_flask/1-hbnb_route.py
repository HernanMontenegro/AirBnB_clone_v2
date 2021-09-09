#!/usr/bin/python3
''' First time with Flask '''
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def hello_hbnb():
    ''' Return the desired string '''
    return "Hello HBNB!"
@app.route('/hbnb')
def hello_hbnb():
    ''' Return the desired string '''
    return "HBNB"

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
