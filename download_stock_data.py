'''
This module is to download and save IPO data from web sites.
'''

import pandas
import requests
from bs4 import BeautifulSoup
from flask import Flask
from string import *

import datetime
import numbers
import urllib
import json
import copy

#get ipo data

#getting url for each month of ipo data
base_url = "https://api.nasdaq.com/api/ipo/calendar?dates="
base_year = 1999
for i in range(base_year, datetime.datetime.now().year + 1):
    for j in range (1, 13):
        if j < 10:
            url = base_url + str(i) + "-0" + str(j)
        else:
            url = base_url + str(i) + "-" + str(j)
        req = urllib.request.Request(url)
