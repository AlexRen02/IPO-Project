'''
This is for setting up the database and be able to pull data from the database.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, create_engine
import json
from config import app

db = SQLAlchemy(app)

class IPO(db.Model):
    __tablename__ = "IPOs"
    id = db.Column(db.Integer, primary_key=True)
    stock_ticker = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=False)
    offer_price = db.Column(db.Double)
    shares = db.Column(db.Integer)
    date = db.Column(db.String)
    offer_amount = db.Column(db.Double)
    ipo_day_open = db.Column(db.Double)
    ipo_day_high = db.Column(db.Double)
    ipo_day_low = db.Column(db.Double)
    ipo_day_close = db.Column(db.Double)

