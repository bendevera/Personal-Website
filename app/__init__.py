from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


APP = Flask(__name__)
APP.config.from_object(Config)
db = SQLAlchemy(APP)
migrate = Migrate(APP, db)


from app import routes, models