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