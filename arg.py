import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
@app.route('/index')
def arg():
    return "hello args"

