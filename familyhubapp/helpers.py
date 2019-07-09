import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from datetime import datetime

def getBool(post_request, name):
    return True if post_request.get(name) else False

class Helpers:
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

    @staticmethod
    def format_description(rawDescrip):
        """ formats description for display in listing pages """
        description = (rawDescrip).split('\r\n')
        index = 0
        descrpDict = []
        for paragraph in description:
            key = str(index)
            descrpDict.append({key:paragraph})
            index = index + 1
        return descrpDict

    @staticmethod
    def format_time(data):
        """ 
        takes time input from post_request and formats
        it into datetime to store in mongodb 
        """
        time = data.split('/')
        time = f"{time[2]}-{time[1]}-{time[0]}"
        time = datetime.strptime(time, '%Y-%m-%d')
        return time

    @staticmethod
    def remove_http(url):
        """ removes https: and http: from all urls passed to the database """
        url = url.replace("https:", "")
        url = url.replace("http:", "")
        return url

    @staticmethod
    def add_https(url):
        """ adds https: to all urls so they are uniform (no http:) """
        url = "https:" + url
        return url

    @staticmethod
    def map_url(activity):
        """ creates url for google maps from the address provided """
        address = activity["address"]["addressLine1"]
        postcode = activity["address"]["postcode"]
        town = activity["address"]["town"]

        address_split = address.replace(' ', '+')
        postcode_split = postcode.replace(' ', '+')
        town_split = town.replace(' ', '+')

        url = 'https://www.google.com/maps/search/?api=1&query=' + address_split + '+' + postcode_split + '+' + town_split
        return url
        

        
