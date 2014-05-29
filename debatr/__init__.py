import os
from flask import Flask, session
import datetime
import bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask import render_template

app = Flask(__name__)
app.config.from_object('debatr.config')
app.secret_key = '\xeb\xca\x0bb\xdb\xa1\x8c\xf4@6Ar H%\xb00\xd8(\x81\xa4\xf8\xa5\xee'
#['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/deb.db"
db = SQLAlchemy(app)

import debatr.views, debatr.models


login_manager = LoginManager()
login_manager.init_app(app)


