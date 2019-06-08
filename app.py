import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords

# create instance of flask and assign it to "app"
app = Flask(__name__)
app.config.from_object(Config)

# MongoDB URI / Assign db
client = MongoClient(Config.MONGO_URI)
db = client.familyHub

# Home page
@app.route('/')
@app.route('/index')
def home_page():
    loggedIn = True if 'user' in session else False

    return render_template("pages/index.html", 
                            title="Home", 
                            active="home",
                            loggedIn=loggedIn,
                            keywords=Keywords.home())

# Activities page
@app.route('/activities')
def activities_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/activities.html", 
                            title="Activities", 
                            active="activities",
                            loggedIn=loggedIn,
                            keywords=Keywords.activities())

# Events page
@app.route('/events')
def events_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/events.html",
                            title="Events", 
                            active="events",
                            loggedIn=loggedIn,
                            keywords=Keywords.events())

# Contact page
@app.route('/contact')
def contact_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/contact.html", 
                            title="Contact", 
                            active="contact",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

@app.route('/newaccount', methods=['GET', 'POST'])

# new_account_page takes data collected with fetch in JS, checks if user already exists in the database
# if not then it encrypts the password before sending complete object to mongodb.
# It then returns to JS if the user already existed or not so JS can provide feedback to the user based on that condition.
# page also renders the newaccount page to be viewed

def new_account_page():
    # -------------------------------------------------------- you don't have permission if not logged in page
    if request.method == 'POST':
        post_request = request.get_json()

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
        
        return json.dumps(response)

    return render_template('pages/newaccount.html', 
                            title="Create Account", 
                            active="newAccount",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# login page
@app.route('/login', methods=['GET', 'POST'])

# login_page takes data collected with fetch in JS, checks if user exists in the database
# If the user is in the database it then compares the password provided with the hashed one from the database
# If the password is correct the value of passwordCorrect is set to True
# All this data is then returned to JS to respond accordingly to the browser

def login_page():

    loggedIn = True if 'user' in session else False
    # check if user is not already logged in
    if loggedIn:
        user_in_db = db.users.find_one({"username": session['user']})
        if user_in_db:
            # If already logged in, redirect user to account page
            return redirect(url_for('my_account_page', user=user_in_db['username']))

    if request.method == 'POST':
        # gets data from form from JS
        post_request = request.get_json()

        # checks user input against usernames in the database
        
        user = db.users.find_one({ '$or': [ { 'username': post_request['loginInput'] }, { 'email': post_request['loginInput'] } ]})
        print(user)

        passwordCorrect = False
        username = ' '

        if user: 
            # check if passwords match, 
            if check_password_hash(user['password'], post_request['password']):
                # Log user in (add to session)
                session['user'] = user['username']
                passwordCorrect = True    
                username = user['username']    

        response = {
            "userMatch": True if user else False,
            "passwordCorrect": passwordCorrect,
            "username": username
        }
        return json.dumps(response)

    return render_template("pages/login.html", 
                            title="Log In", 
                            active="login",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# log out page
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for('home_page'))

# Search page
@app.route('/search')
def search_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/search.html", 
                            title="Search",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Activity listing page - see if possible to update this to different routes based on each activity title
@app.route('/activity-listing')
def activity_listing_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/activitylisting.html", 
                            title="Activity Listing",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Event listing page - see if possible to update this to different routes based on each event title
@app.route('/event-listing')
def event_listing_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/eventlisting.html", 
                            title="Event Listing",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Search page
@app.route('/settings')
def settings_page():
    #---------------------------------------------------- permission
    return render_template("pages/settings.html", 
                            title="Account Settings", 
                            keywords=Keywords.generic())

# Account page - all listings for this account
@app.route('/account')
def my_account_page():
    #---------------------------------------------------- permission
    return render_template("pages/account.html", 
                            title="My Account", 
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Add new event page
@app.route('/add-new-event')
def new_event_page():
    #---------------------------------------------------- permission
    return render_template("pages/addevent.html", 
                            title="Add New Event", 
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Edit existing event page
@app.route('/edit-event')
def edit_event_page():
    #---------------------------------------------------- permission
    return render_template("pages/editevent.html", 
                            title="Edit Event", 
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Add new activity page
@app.route('/add-new-activity')
def new_activity_page():
    #---------------------------------------------------- permission
    return render_template("pages/addactivity.html", 
                            title="Add New Activity", 
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# Edit existing activity page
@app.route('/edit-activity')
def edit_activity_page():
    #---------------------------------------------------- permission
    return render_template("pages/editactivity.html", 
                            title="Edit Activity", 
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
            port=os.getenv('PORT'), 
            debug=True)
