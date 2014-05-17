import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Resolution(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	full = db.Column(db.String(200)
        category = db.Column(db.String(200))

        def __init__(self, name, full, cat)
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

        def __init__(self,debID, teamID, text, argType, raID)
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

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	email = db.Column(db.String(50))
	pass = db.Column(db.String(200))
	salt = db.Column(db.String(100))




