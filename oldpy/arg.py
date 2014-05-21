import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)

from app import views, models


@app.route('/')
@app.route('/index')
def arg():
    return "hello args"

