import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
from app import views


@app.route('/')
@app.route('/index')
def arg():
    return "hello args"


