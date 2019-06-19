import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from datetime import datetime

class Helpers:

    @staticmethod
    def getPost(post_request, name):
        return True if post_request.get(name) else False

    """ 
    loops through open/close times and converts datetimes for display in browser
    leaves other values as None to make it easier to print out on screen
    """
    @staticmethod
    def open_times(openTimes_db):
        openTimes = []
        for key, time in openTimes_db.items():
            if time != None:
                fTime = time.strftime("%H:%M")
                openTimes.append({key:fTime})
            else:
                openTimes.append({key:time})

        return openTimes

    """
    formats description for display in listing pages
    """
    @staticmethod
    def format_description(rawDescrip):
        description = (rawDescrip).split('\r\n')

        index = 0
        descrpDict = []
        for paragraph in description:
            if paragraph != '':  
                key = str(index)
                descrpDict.append({key:paragraph})
                index = index + 1

        return descrpDict