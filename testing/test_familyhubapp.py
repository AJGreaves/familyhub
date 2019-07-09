import os, unittest, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, slugify
from familyhubapp.helpers import Helpers
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

def testSlugify():
    capitals = slugify('CAPITALS')
    MyStrinG = slugify('MyStrinG')
    spaces = slugify('string with spaces in')
    assert capitals == 'capitals', 'slugify() should return string with all capitals changed to lowercase'
    assert MyStrinG == 'mystring', 'slugify() should return string with mix of capitals and lowercase changed to all lowercase'
    assert spaces == 'string-with-spaces-in', 'slugify() should return string where any spaces have been replaced with -'

testSlugify()

def test_open_times():
    openTimes_db = {
        'monStart': None, 
        'monEnd': None, 
        'tueStart': None, 
        'tueEnd': None, 
        'wedStart': datetime(1900, 1, 1, 15, 30), 
        'wedEnd': datetime(1900, 1, 1, 17, 0), 
        'thuStart': None, 
        'thuEnd': None, 
        'friStart': None, 
        'friEnd': None, 
        'satStart': datetime(1900, 1, 1, 10, 0), 
        'satEnd': datetime(1900, 1, 1, 11, 30), 
        'sunStart': datetime(1900, 1, 1, 10, 0), 
        'sunEnd': datetime(1900, 1, 1, 16, 30)
    }
    openTimes = Helpers.open_times(openTimes_db)
    expectedResult = [
        {'monStart': None}, 
        {'monEnd': None}, 
        {'tueStart': None}, 
        {'tueEnd': None}, 
        {'wedStart': '15:30'}, 
        {'wedEnd': '17:00'}, 
        {'thuStart': None}, 
        {'thuEnd': None}, 
        {'friStart': None}, 
        {'friEnd': None}, 
        {'satStart': '10:00'}, 
        {'satEnd': '11:30'}, 
        {'sunStart': '10:00'}, 
        {'sunEnd': '16:30'}
    ]
    assert openTimes == expectedResult, "open_times() should return array of objects with datetime objects converted into times to display"

test_open_times()

print("All tests passed")
