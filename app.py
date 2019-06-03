import os
from flask import Flask, redirect, render_template, request, url_for
from app.keys import Keywords

# create instance of flask and assign it to "app"
app = Flask(__name__) 

# Home page
@app.route('/')
def home_page():
    return render_template("index.html", 
                            title="Home", 
                            active="home",
                            keywords=Keywords.home)

# Activities page
@app.route('/activities')
def activities_page():
    return render_template("activities.html", 
                            title="Activities", 
                            active="activities",
                            keywords=Keywords.activities)

# Events page
@app.route('/events')
def events_page():
    return render_template("events.html",
                            title="Events", 
                            active="events",
                            keywords=Keywords.events)

# Contact page
@app.route('/contact')
def contact_page():
    return render_template("contact.html", 
                            title="Contact", 
                            active="contact",
                            keywords=Keywords.generic)

# Create Account page
@app.route('/newaccount')
def new_account_page():
    return render_template("newaccount.html", 
                            title="Create Account", 
                            active="newAccount",
                            keywords=Keywords.generic)

# Contact page
@app.route('/login')
def login_page():
    return render_template("login.html", 
                            title="Log In", 
                            active="login",
                            keywords=Keywords.generic)

# Search page
@app.route('/search')
def search_page():
    return render_template("search.html", 
                            title="Search",
                            keywords=Keywords.generic)

# Activity listing page - see if possible to update this to different routes based on each activity title
@app.route('/activity-listing')
def activity_listing_page():
    return render_template("activitylisting.html", 
                            title="Activity Listing",
                            keywords=Keywords.generic)

# Event listing page - see if possible to update this to different routes based on each event title
@app.route('/event-listing')
def event_listing_page():
    return render_template("eventlisting.html", 
                            title="Event Listing",
                            keywords=Keywords.generic)

# Search page
@app.route('/settings')
def settings_page():
    return render_template("settings.html", 
                            title="Account Settings", 
                            loginStatus=True,
                            keywords=Keywords.generic)

# Account page - all listings for this account
@app.route('/account')
def my_account_page():
    return render_template("account.html", 
                            title="My Account", 
                            loginStatus=True,
                            keywords=Keywords.generic)

# Add new event page
@app.route('/add-new-event')
def new_event_page():
    return render_template("addevent.html", 
                            title="Add New Event", 
                            loginStatus=True,
                            keywords=Keywords.generic)

# Add new activity page
@app.route('/add-new-activity')
def new_activity_page():
    return render_template("addactivity.html", 
                            title="Add New Activity", 
                            loginStatus=True,
                            keywords=Keywords.generic)

# Edit existing activity page
@app.route('/edit-activity')
def edit_activity_page():
    return render_template("editactivity.html", 
                            title="Edit Activity", 
                            loginStatus=True,
                            keywords=Keywords.generic)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
            port=os.getenv('PORT'), 
            debug=True)
