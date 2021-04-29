import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from instance.config import app_config

db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config.from_pyfile('config.py')
db.init_app(app)
ma = Marshmallow(app)


from app.team import views
