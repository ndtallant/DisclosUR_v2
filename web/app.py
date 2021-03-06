'''
    app.py
    ------

    Author: ndtallant

    Description: This file is the server logic for the website.
'''
from flask import Flask, render_template, url_for, session, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Legislator, Interest

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page of the webapp."""
    return render_template('index.html')

@app.route('/results')
def results():
    """Returns the legislators and relevant information."""
    legislators = Legislator.query.all()[:20]
    return render_template('results.html', legislators=legislators)

@app.route('/about')
def about():
    """Simply renders the about page."""
    return render_template('about.html')
