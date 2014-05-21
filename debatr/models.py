import os
from flask import Flask
import datetime
import bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from debatr import app

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Resolution(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	full = db.Column(db.String(200))
    category = db.Column(db.String(200))

    def __init__(self, name, full, cat):
		self.name = name
		self.full = full
		self.category = cat

class Argument(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    debID = db.Column(db.Integer)
    teamID = db.Column(db.Integer)
    text = db.Column(db.Text)
    argType = db.Column(db.String(200))
    relatedArgID = db.Column(db.Integer)

    def __init__(self,debID, teamID, text, argType, raID):
		self.debID = debID
        self.teamID = teamID
        self.text = text
        self.argType = argType
        self.relatedArgID = raID

class Debate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
    proTeamID = db.Column(db.Integer)
    conTeamID = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, name, proID, conID, date=datetime.datetime.now()):
		self.name = name
		self.proTeamID = proID
		self.conTeamID = conID
		self.date = date

class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	memberList = db.Column(db.Text)

	def __init__(self, name, memlist):
		self.name = name
		self.memberList = memlist

class Fact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	argID = db.Column(db.Integer)
	text = db.Column(db.Text)
	link = db.Column(db.String(100))

	def __init__(self, arg, text, link):
		self.argID = arg
		self.text = text
		self.link = link

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	email = db.Column(db.String(50))
	password = db.Column(db.String(200))
	salt = db.Column(db.String(100))

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		#self.password = password
		self.set_password(self, password)
	
	def set_password(self, password):
		self.pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())

	def check_password(self, password):
		if bcrypt.hashpw(password, self.pw_hash) == self.pw_hash:
			return True
		else:
			return False

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.name)


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	cType = db.Column(db.String(40))
	cRefID = db.Column(db.Integer)
	cText = db.Column(db.Text)

	def __init__(self, ctype, refID, text):
		self.cType = ctype
		self.cRefID = refID
		self.cText = text





