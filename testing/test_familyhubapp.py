import os, sys
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
    openTimes = Helpers.open_times(openTimes_db)
    assert openTimes == expectedResult, "open_times() should return array of objects with datetime objects converted into times to display"

test_open_times()

def test_format_description():
    rawDescrip1 = 'Line 1\r\nLine 2\r\nLine 3'
    expected_result1 = [{'0': 'Line 1'}, {'1': 'Line 2'}, {'2': 'Line 3'}]
    result1 = Helpers.format_description(rawDescrip1)
    assert result1 == expected_result1, "format_description() should return array of objects separated into paragraphs"

    rawDescrip2 = 'Line 1\r\n\r\nLine 2\r\n\r\nLine 3'
    expected_result2 = [{'0': 'Line 1'}, {'1': ''}, {'2': 'Line 2'}, {'3': ''}, {'4': 'Line 3'}]
    result2 = Helpers.format_description(rawDescrip2)
    assert result2 == expected_result2, "format_description() should empty paragraphs for double line breaks"

test_format_description()

def test_format_time():
    data = '17/07/2019'
    expected_time = '2019-07-17 00:00:00'
    time = Helpers.format_time(data)
    time_str = str(time)
    assert time_str == expected_time, 'format_time() should return datetime formatted string'

test_format_time()

def test_remove_http():
    expected_result = '//www.google.com/'

    url_input1 = 'https://www.google.com/'
    result1 = Helpers.remove_http(url_input1)
    assert result1 == expected_result, 'remove_http() should return url with https: removed'

    url_input2 = 'http://www.google.com/'
    result2 = Helpers.remove_http(url_input2)
    assert result2 == expected_result, 'remove_http() should return url with http: removed'

test_remove_http()

def test_add_https():
    expected_result = 'https://www.google.com/'

    url_input = '//www.google.com/'
    result = Helpers.add_https(url_input)
    assert result == expected_result, 'add_https() should return url with https: added to beginning'

test_add_https()

print("All tests passed")
