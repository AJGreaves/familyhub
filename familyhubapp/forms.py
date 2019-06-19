import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from datetime import datetime
from familyhubapp.helpers import Helpers, getPost

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

def process_event_data(db, user, post_request, published):
    """
    Processed dict post_request so that it is correct to insert into the database.
    Processes date information to turn it into format needed to store date in mongodb.
    Processes number string into int for storing correctly.
    creates new object with username from post_request dict, username from database and
    all boolean values converted as needed to be store correctly in the database, returns 
    obj to be inserted into the database.
    """
    # credit for date processing code to fellow student Seán Murphy 
    date = post_request['date'].split('/')
    date = f"{date[2]}-{date[1]}-{date[0]}"
    date = datetime.strptime(date, '%Y-%m-%d')

    if post_request.get('from'):
        price_string = post_request.get('from')
        price_int = int(price_string)

    obj = {
        'username': user['username'], 
        'title': post_request.get('title'),
        'imgUrl': post_request.get('imgUrl'),
        'date': date, 
        'address': {
            'addressLine1': getPost(post_request, 'addressLine1'),
            'postcode': getPost(post_request, 'postcode'),
            'town': getPost(post_request, 'town'),
        },
        'ageRange': {
            'under4': getPost(post_request, 'under4'),
            'age4to6': getPost(post_request, 'age4to6'),
            'age6to8': getPost(post_request, 'age6to8'),
            'age8to10': getPost(post_request, 'age8to10'),
            'age10to12': getPost(post_request, 'age10to12'),
            'age12up': getPost(post_request, 'age12up'),
        },
        'price': {
            'from': price_int if post_request.get('from') else None,
            'isFree': getPost(post_request, 'isFree')
        },
        'indoor': getPost(post_request, 'indoor'),
        'outdoor': getPost(post_request, 'outdoor'),
        'contact': {
            'url': post_request.get('url'),
            'email': post_request.get('email'),
            'facebook': post_request.get('facebook') if post_request.get('facebook') else None,
            'twitter': post_request.get('twitter') if post_request.get('twitter') else None,
            'instagram': post_request.get('instagram') if post_request.get('instagram') else None
        },
        'description': post_request.get('description'),
        'published': published
    }

    return obj

