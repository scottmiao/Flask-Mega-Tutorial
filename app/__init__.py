from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'  # Flask-Login needs to know what view logs users in.
oid = OpenID(app, os.path.join(basedir, 'tmp'))
