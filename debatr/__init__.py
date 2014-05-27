import os
from flask import Flask
import datetime
import bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/deb.db"
db = SQLAlchemy(app)

import debatr.views #, debatr.models

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)
#login_manager = LoginManager()
#login_manager.init_app(app)


