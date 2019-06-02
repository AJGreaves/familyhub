import os
from flask import Flask, render_template, redirect, request, url_for, request

# create instance of flask and assign it to "app"
app = Flask(__name__) 

# Home page
@app.route('/')
def home_page():
    return render_template("index.html", title="Home", active="home")

# Activities page
@app.route('/activities')
def activities_page():
    return render_template("activities.html", title="Activities", active="activities")

# Events page
@app.route('/events')
def events_page():
    return render_template("events.html", title="Events", active="events")

# Contact page
@app.route('/contact')
def contact_page():
    return render_template("contact.html", title="Contact", active="contact")

# Create Account page
@app.route('/newaccount')
def new_account_page():
    return render_template("newaccount.html", title="Create Account", active="newAccount")

# Contact page
@app.route('/login')
def login_page():
    return render_template("login.html", title="Log In", active="login")

# Search page
@app.route('/search')
def search_page():
    return render_template("search.html", title="Search")

# Activity listing page - see if possible to update this to different routes based on each activity title
@app.route('/activity-listing')
def activity_listing_page():
    return render_template("activitylisting.html", title="Activity Listing")

# Event listing page - see if possible to update this to different routes based on each event title
@app.route('/event-listing')
def event_listing_page():
    return render_template("eventlisting.html", title="Event Listing")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)