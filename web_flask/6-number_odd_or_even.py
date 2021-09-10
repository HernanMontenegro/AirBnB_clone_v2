#!/usr/bin/python3
''' First time with Flask '''
from flask import Flask, render_template


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

@app.route('/python/<text>')
@app.route('/python')
def Python_is_fun(text="is cool"):
    ''' Return the desired string '''
    text.replace('_', ' ')
    return "Python " + text

@app.route('/number/<int:n>')
def display_if_integer(n):
    ''' Return the desired string '''
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def display_if_integer_template(n):
    ''' Return the desired string '''
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def display_if_integer_template_ans(n):
    ''' Return the desired string '''
    ans = "even"
    if (n % 2 != 0):
        ans = "odd"
    return render_template('6-number_odd_or_even.html', n=n, answer=ans)

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
