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
	debates = Debate.query.limit(1).all()[0]
	res = Resolution.query.filter_by(id=debates.resID).all()[0]
	proTeam = Team.query.filter_by(id=debates.proTeamID).all()[0]
	conTeam = Team.query.filter_by(id=debates.conTeamID).all()[0]
	proargs = Argument.query.filter_by(debID=debates.id).filter_by(teamID=proTeam.id).all()
	conargs = Argument.query.filter_by(debID=debates.id).filter_by(teamID=conTeam.id).all()
	return render_template('debate.html', resolution = res, pro = proTeam, con = conTeam, proarg = proargs, conarg = conargs)


