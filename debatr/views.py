import os
from flask import Flask
import datetime
import bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import render_template
from debatr import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/debate')
def debate():
	return render_template('debate.html')


