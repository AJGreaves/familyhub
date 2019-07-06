import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from datetime import datetime
from familyhubapp.helpers import Helpers, getBool

def new_account_req(db, post_request):
    """
    Takes post_request data collected with fetch in JS, checks if user already 
    exists in the database. if they are send message back to js to give feedback to the user.
    if they are not then it encrypts the password before sending complete object to mongodb.
    It then returns to JS if the user already existed or not so JS can provide feedback to the user based on that condition.
    page also renders the newaccount page to be viewed
    """
    emailExists = True
    userExists = True

    user_email = db.users.find_one({"email": post_request['email']})
    user_username = db.users.find_one({"username": post_request['username']})

    if not user_email:
        emailExists = False
    elif not user_username:
        userExists = False

    if not user_username and not user_email:
        userExists = False
        emailExists = False
        post_request['password'] = generate_password_hash(post_request['password'])
        db.users.insert_one(post_request)

    response = {
        "emailExists": emailExists,
        "userExists": userExists,
        "username": post_request['username']
    }

    return response

def login_req(db, post_request):
    """
    Finds existing user in the database based on their input, compares the data.
    Returns appropriate response to be sent to JS to trigger modal message for the user. 
    """
    user = db.users.find_one({ '$or': [ { 'username': post_request['loginInput'] }, { 'email': post_request['loginInput'] } ]})
    passwordCorrect = False
    username = ''

    if user: 
        if check_password_hash(user['password'], post_request['password']):
            session['user'] = user['username']
            passwordCorrect = True    
            username = user['username']    

    response = {
        "userMatch": True if user else False,
        "passwordCorrect": passwordCorrect,
        "username": username
    }

    return response

def settings_update(db, user, post_request):
    """
    Collects the input from the settings page which requests a change to the users email or password. 
    compares the input sent. To check that the old email address provided matches the one in the database
    before updating it. Same for the password change. response is sent back to JS to control what alerts/messages
    are returned to the user, in case they enter an incorrect password or email. 
    """
    updated = False

    if post_request['whichForm'] == 'emai':
        if user['email'] == post_request['oldInput']:
            db.users.find_one_and_update({"_id": ObjectId(user["_id"])}, {"$set": {"email": post_request["newInput"]}})
            updated = True
    
    if post_request['whichForm'] == 'pass':
        if check_password_hash(user['password'], post_request['oldInput']):
            post_request['newInput'] = generate_password_hash(post_request['newInput'])
            db.users.find_one_and_update({"_id": ObjectId(user["_id"])}, {"$set": {"password": post_request["newInput"]}})
            updated = True

    response = {
        "updated": updated
    }

    return response

def process_activity_data(db, user, post_request, published):
    """
    Processes date information to turn it into format needed to store date in mongodb.
    Processes times by first looping through all the possible times, turning them into the correct format for
    mongo and then adding them to a new dict to use to construct the final object to send to mongo.
    creates new object with username from post_request dict, username from database and
    all boolean values converted as needed to be store correctly in the database,
    """

    start = Helpers.format_time(post_request['start']) if getBool(post_request, 'start') else None
    end = Helpers.format_time(post_request['end']) if getBool(post_request, 'start') else None
    description = post_request.get('description')
    shortDescription = description[0:100]
    imgUrl = Helpers.remove_http(post_request.get('imgUrl'))
    url = Helpers.remove_http(post_request.get('url'))
    if post_request.get('facebook'):
        facebook = Helpers.remove_http(post_request.get('facebook'))
    if post_request.get('instagram'):
        instagram = Helpers.remove_http(post_request.get('instagram'))
    if post_request.get('twitter'):
        twitter = Helpers.remove_http(post_request.get('twitter'))

    openTimes = [
        'monStart','monEnd', 'tueStart', 'tueEnd', 
        'wedStart', 'wedEnd', 'thuStart', 'thuEnd',
        'friStart', 'friEnd', 'satStart', 'satEnd',
        'sunStart', 'sunEnd'
    ]

    openTimesDict = { }

    for time_name in openTimes:
        if post_request.get(time_name):
            time = time_name
            time = post_request[time].split(':')
            time = f"{time[0]}:{time[1]}:00"
            time = datetime.strptime(time, '%H:%M:%S')
            openTimesDict[time_name] = time


    obj = {
        'username': user['username'], 
        'title': post_request.get('title'),
        'imgUrl': imgUrl,
        'dates': { 
            'start': start, 
            'end': end,
            'ongoing': getBool(post_request, 'ongoing'),
        },
        'days' : {
            'mon': getBool(post_request, 'mon'),
            'tue': getBool(post_request, 'tue'),
            'wed': getBool(post_request, 'wed'),
            'thu': getBool(post_request, 'thu'),
            'fri': getBool(post_request, 'fri'),
            'sat': getBool(post_request, 'sat'),
            'sun': getBool(post_request, 'sun')
        },
        'times': {
            'monStart': openTimesDict.get('monStart') if openTimesDict.get('monStart') else None,
            'monEnd': openTimesDict.get('monEnd') if openTimesDict.get('monEnd') else None,
            'tueStart': openTimesDict.get('tueStart') if openTimesDict.get('tueStart') else None,
            'tueEnd': openTimesDict.get('tueEnd') if openTimesDict.get('tueEnd') else None,
            'wedStart': openTimesDict.get('wedStart') if openTimesDict.get('wedStart') else None,
            'wedEnd': openTimesDict.get('wedEnd') if openTimesDict.get('wedEnd') else None,
            'thuStart': openTimesDict.get('thuStart') if openTimesDict.get('thuStart') else None,
            'thuEnd': openTimesDict.get('thuEnd') if openTimesDict.get('thuEnd') else None,
            'friStart': openTimesDict.get('friStart') if openTimesDict.get('friStart') else None,
            'friEnd': openTimesDict.get('friEnd') if openTimesDict.get('friEnd') else None,
            'satStart': openTimesDict.get('satStart') if openTimesDict.get('satStart') else None,
            'satEnd': openTimesDict.get('satEnd') if openTimesDict.get('satEnd') else None,
            'sunStart': openTimesDict.get('sunStart') if openTimesDict.get('sunStart') else None,
            'sunEnd': openTimesDict.get('sunEnd') if openTimesDict.get('sunEnd') else None
        },
        'holidays' : {
            'spring': getBool(post_request, 'spring'),
            'summer': getBool(post_request, 'summer'),
            'autumn': getBool(post_request, 'autumn'),
            'christmas': getBool(post_request, 'christmas'),
        },
        'categories': {
            'sports': getBool(post_request, 'sports'),
            'swimming': getBool(post_request, 'swimming'),
            'creative': getBool(post_request, 'creative'),
            'scienceTech': getBool(post_request, 'scienceTech'),
            'cultureMusic': getBool(post_request, 'cultureMusic'),
            'dramaDance': getBool(post_request, 'dramaDance'),
            'yogaMindfulness': getBool(post_request, 'yogaMindfulness'),
            'museumsExhibitions': getBool(post_request, 'museumsExhibitions'),
            'parksPlaygrounds': getBool(post_request, 'parksPlaygrounds'),
            'playgroups': getBool(post_request, 'playgroups'),
            'nature': getBool(post_request, 'nature'),
            'animals': getBool(post_request, 'animals'),
            'clubs': getBool(post_request, 'clubs'),
            'parties': getBool(post_request, 'parties'),
        },
        'otherDetails': {
            'free': getBool(post_request, 'free'),
            'bringFood': getBool(post_request, 'bringFood'),
            'catering': getBool(post_request, 'catering'),
            'goodWeather': getBool(post_request, 'goodWeather'),
            'badWeather': getBool(post_request, 'badWeather'),
            'groups': getBool(post_request, 'groups'),
        },
        'address': {
            'addressLine1': post_request.get('addressLine1'),
            'postcode': post_request.get('postcode'),
            'town': post_request.get('town')
        },
        'ageRange': {
            'under4': getBool(post_request, 'under4'),
            'age4to6': getBool(post_request, 'age4to6'),
            'age6to8': getBool(post_request, 'age6to8'),
            'age8to10': getBool(post_request, 'age8to10'),
            'age10to12': getBool(post_request, 'age10to12'),
            'age12up': getBool(post_request, 'age12up')
        },
        'indoor': getBool(post_request, 'indoor'),
        'outdoor': getBool(post_request, 'outdoor'),
        'contact': {
            'phone': post_request.get('phone'),
            'url': url,
            'email': post_request.get('email'),
            'facebook': facebook if post_request.get('facebook') else None,
            'twitter': twitter if post_request.get('twitter') else None,
            'instagram': instagram if post_request.get('instagram') else None
        },
        'description': post_request.get('description'),
        'shortDescription': shortDescription,
        'published': False
    }
    return obj
