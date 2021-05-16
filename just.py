from flask import Flask
import random
app = Flask(__name__)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from flaskr.db import get_db

bp = Blueprint('just', __name__)    #  n'encombre pas

@app.route('/just')
def justwebsite1():
    return render_template('justwebsite1/justindex.html') 

def justparamplace():
    return "Chastre"

@app.route('/')
def justindex():
    randnum = random.randint(1, 100)

#    return render_template('justwebsite1/justindex.html')
    return render_template('base.html', justparamplace=justparamplace(), MLB_team=MLB_team, type=type)

# let'stry having some live parameters : app parameters, not depending on db or session


justparamwriter="Spirou"
justparampostcode=1450


MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
    ])

