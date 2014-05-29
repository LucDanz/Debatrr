import os
from flask import Flask
import datetime
import bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask import render_template, url_for, redirect, flash, request
from debatr import app
from debatr import models

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	username = request.form['username']
	password = request.form['password']
	registered_user = models.User.query.filter_by(name=username).first()
	#if registered_user is None:
	#	flash('Username is invalid', 'error')
	#	return redirect(url_for('login'))
	if registered_user.check_password(password):
		login_user(registered_user)
		flash("Logged in successfully")
		#return redirect(request.args.get('next') or url_for('index'))
		return redirect(url_for('index'))
	else:
		flash('Username or Password is invalid', 'error')
		return redirect(url_for('login'))
		
		
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
		
@app.route('/debate')
#@login_required
def debate():
	debates = models.Debate.query.limit(1).all()[0]
	res = models.Resolution.query.filter_by(id=debates.resID).all()[0]
	proTeam = models.Team.query.filter_by(id=debates.proTeamID).all()[0]
	conTeam = models.Team.query.filter_by(id=debates.conTeamID).all()[0]
	proargs = models.Argument.query.filter_by(debID=debates.id).filter_by(teamID=proTeam.id).all()
	conargs = models.Argument.query.filter_by(debID=debates.id).filter_by(teamID=conTeam.id).all()
	return render_template('debate.html', resolution = res, pro = proTeam, con = conTeam, proarg = proargs, conarg = conargs)


