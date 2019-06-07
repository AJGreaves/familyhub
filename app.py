import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify
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

@app.route('/newaccount', methods=['GET', 'POST'])


# newUser function takes data collected with fetch in JS, checks if user already exists in the database
# if not then it encrypts the password before sending complete object to mongodb.
# It then returns to JS if the user already existed or not so JS can provide feedback to the user based on that condition.
# function also renders the newaccount page to be viewed


def newUser():

    if request.method == 'POST':
        post_request = request.get_json()

        user = db.users.find_one({"email": post_request['email']})
        print(user)

        if not user:
            
            post_request['password'] = generate_password_hash(post_request['password'])
            db.users.insert_one(post_request)

        response = {"response": False if user else True}
        
        return json.dumps(response)

    return render_template('pages/newaccount.html', 
                            title="Create Account", 
                            active="newAccount",
                            keywords=Keywords.generic())

# Home page
@app.route('/')
def home_page():
    return render_template("pages/index.html", 
                            title="Home", 
                            active="home",
                            keywords=Keywords.home())

# Activities page
@app.route('/activities')
def activities_page():
    return render_template("pages/activities.html", 
                            title="Activities", 
                            active="activities",
                            keywords=Keywords.activities())

# Events page
@app.route('/events')
def events_page():
    return render_template("pages/events.html",
                            title="Events", 
                            active="events",
                            keywords=Keywords.events())

# Contact page
@app.route('/contact')
def contact_page():
    return render_template("pages/contact.html", 
                            title="Contact", 
                            active="contact",
                            keywords=Keywords.generic())

# Create Account page
@app.route('/newaccount')
def new_account_page():
    return render_template("pages/newaccount.html", 
                            title="Create Account", 
                            active="newAccount",
                            keywords=Keywords.generic())

# Contact page
@app.route('/login')
def login_page():
    return render_template("pages/login.html", 
                            title="Log In", 
                            active="login",
                            keywords=Keywords.generic())

# Search page
@app.route('/search')
def search_page():
    return render_template("pages/search.html", 
                            title="Search",
                            keywords=Keywords.generic())

# Activity listing page - see if possible to update this to different routes based on each activity title
@app.route('/activity-listing')
def activity_listing_page():
    return render_template("pages/activitylisting.html", 
                            title="Activity Listing",
                            keywords=Keywords.generic())

# Event listing page - see if possible to update this to different routes based on each event title
@app.route('/event-listing')
def event_listing_page():
    return render_template("pages/eventlisting.html", 
                            title="Event Listing",
                            keywords=Keywords.generic())

# Search page
@app.route('/settings')
def settings_page():
    return render_template("pages/settings.html", 
                            title="Account Settings", 
                            loginStatus=True,
                            keywords=Keywords.generic())

# Account page - all listings for this account
@app.route('/account')
def my_account_page():
    return render_template("pages/account.html", 
                            title="My Account", 
                            loginStatus=True,
                            keywords=Keywords.generic())

# Add new event page
@app.route('/add-new-event')
def new_event_page():
    return render_template("pages/addevent.html", 
                            title="Add New Event", 
                            loginStatus=True,
                            keywords=Keywords.generic())

# Edit existing event page
@app.route('/edit-event')
def edit_event_page():
    return render_template("pages/editevent.html", 
                            title="Edit Event", 
                            loginStatus=True,
                            keywords=Keywords.generic())

# Add new activity page
@app.route('/add-new-activity')
def new_activity_page():
    return render_template("pages/addactivity.html", 
                            title="Add New Activity", 
                            loginStatus=True,
                            keywords=Keywords.generic())

# Edit existing activity page
@app.route('/edit-activity')
def edit_activity_page():
    return render_template("pages/editactivity.html", 
                            title="Edit Activity", 
                            loginStatus=True,
                            keywords=Keywords.generic())

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
            port=os.getenv('PORT'), 
            debug=True)
