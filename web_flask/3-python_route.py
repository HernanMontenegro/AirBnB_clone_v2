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
def hbnb():
    ''' Return the desired string '''
    return "HBNB"

@app.route('/c/<text>')
def C_is_fun(text):
    ''' Return the desired string '''
    text.replace('_', ' ')
    return "C " + text

@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/(<text>)')
def Python_is_fun(text):
    ''' Return the desired string '''
    text.replace('_', ' ')
    return "Python " + text

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
