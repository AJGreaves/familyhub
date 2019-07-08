import os, unittest, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app
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

class TestRoutes(unittest.TestCase):
    def setUp(self):

        self.client = app.test_client()

    def test_routes(self):

        response = self.client.get('/')
        data = response.data.decode('utf-8')
        assert response.status_code == 200