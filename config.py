from flask import Flask
from logging import DEBUG

class Config:
    ENV="dev"
    AppName="IPO Predictor"
    DEFAULT_PAGE_LIMIT = 5
    # Alex's local DB
    DB_URI = "sqlite:////Users/alexren/projects/ProjectIPO/db"
    # Wilmer's local DB
    # DB_URI = ""
    # Production DB
    # DB_URI = ""


app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = Config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'ipopredictor'
app.logger.setLevel(DEBUG)
