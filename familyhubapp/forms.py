import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from datetime import datetime

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