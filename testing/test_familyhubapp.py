import os, unittest
from app import app
from pymongo import MongoClient
from bson.objectid import ObjectId

# config
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = 'SECRET_KEY_SK'
app.config["WTF_CSRF_ENABLED"] = False
app.config['TESTING'] = True

# configure mongo
client = MongoClient('localhost', 27017)

# database / collections
db = client.familyHub
activities = db.activities
users = db.users
