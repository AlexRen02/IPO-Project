'''
This module is to download and save IPO data from web sites.
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from string import *

import numbers
import urllib
import json
import copy

#get ipo data
base_url = "https://www.nasdaq.com/market-activity/ipos"
#html parse table
#using ipo ticker search for day data