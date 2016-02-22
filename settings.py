# -*- coding: UTF-8 -*-

import os
import redis
from pymongo import MongoClient

# set python path from env variable
PYTHONPATH = os.environ["PYTHONPATH"]

"""
client id and secret can be found here:
https://groups.google.com/forum/#!forum/feedly-cloud
NOTE: client secret is updated every couple of months for sandbox
"""
# can only redirect to specific URIs - see the forum above
FEEDLY_REDIRECT_URI = "http://localhost:8080"
FEEDLY_CLIENT_ID = "sandbox"
FEEDLY_CLIENT_SECRET = os.environ.get("FEEDLY_CLIENT_SECRET")
ALCHEMY_API_KEY = "fadb2a3e8250eb5ba9c6cbdd66781322e1861ec5"

# ID can be found at: GET /v3/profile
# http://developer.feedly.com/v3/profile/
#TODO: create user table and store with email, etc..
USER_ID = "d2eb5e88-3736-40ad-870c-e6b831480e8b"

# DATABASE SETTINGS

# mongodb initialization
mongo = MongoClient('localhost', 27017)
db = mongo.development
# redis initialization
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)

# ALCHEMY
APILIMIT = 1000
API_BASE_URL = 'http://gateway-a.watsonplatform.net/calls/url/URLGetTextSentiment'
