#!/usr/bin/python3
'''First time with Flask'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closeame():
    '''closeame'''
    storage.close()


@app.route('/states_list')
def States():
    ''' List of all states '''
    list_states = storage.all(State).values()
    return render_template('7-states_list.html', list_states=list_states)
