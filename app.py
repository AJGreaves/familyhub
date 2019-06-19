import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from familyhubapp.helpers import Helpers
from familyhubapp.forms import new_account_req, login_req, settings_update, process_event_data, process_activity_data
from datetime import datetime

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

    return render_template(
        "pages/index.html", 
        headTitle="Home", 
        active="home",
        loggedIn=loggedIn,
        keywords=Keywords.home()
    )

# Activities page
@app.route('/activities')
def activities_page():
    loggedIn = True if 'user' in session else False
    return render_template(
        "pages/activities.html", 
        headTitle="Activities", 
        active="activities",
        loggedIn=loggedIn,
        keywords=Keywords.activities()
    )

# Events page
@app.route('/events')
def events_page():
    loggedIn = True if 'user' in session else False
    return render_template(
        "pages/events.html",
        headTitle="Events", 
        active="events",
        loggedIn=loggedIn,
        keywords=Keywords.events()
    )

# Contact page
@app.route('/contact')
def contact_page():
    loggedIn = True if 'user' in session else False
    return render_template(
        "pages/contact.html", 
        headTitle="Contact", 
        active="contact",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# new account page
@app.route('/newaccount', methods=['GET', 'POST'])
def new_account_page():
    """ Checks if user is already logged in, if they are redirects them to their account page """
    loggedIn = True if 'user' in session else False

    if loggedIn:
        user_in_db = db.users.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('my_account_page', user=user_in_db['username']))

    if request.method == 'POST':
        post_request = request.get_json()
        response = new_account_req(db, post_request)
        return json.dumps(response)

    return render_template(
        'pages/newaccount.html', 
        headTitle="Create Account", 
        active="newAccount",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    loggedIn = True if 'user' in session else False

    if loggedIn == True:
        user_in_db = db.users.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('my_account_page', user=user_in_db['username']))

    if request.method == 'POST':
        post_request = request.get_json()
        response = login_req(db, post_request)
        return json.dumps(response)

    return render_template(
        "pages/login.html", 
        headTitle="Log In", 
        active="login",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

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
    return render_template(
        "pages/search.html", 
        headTitle="Search",
        active="search",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# Activity listing page 
@app.route('/activity-listing/<title>')
def activity_listing_page(title):
    loggedIn = True if 'user' in session else False

    activity_id = request.args.get('activity_id')
    newActivity = request.args.get('newActivity')

    activity = db.activities.find_one({"_id": ObjectId(activity_id)})
    startDate = activity["dates"]['start'].strftime("%d %b %Y")
    endDate = activity["dates"]['end'].strftime("%d %b %Y")
    openTimes_db = activity['times']
    rawDescrip = activity['description']

    openTimes = Helpers.open_times(openTimes_db)
    descrpDict = Helpers.format_description(rawDescrip)

    return render_template(
        "pages/activitylisting.html", 
        headTitle="Activity Listing",
        title=title,
        activity=activity,
        startDate=startDate,
        endDate=endDate,
        description=descrpDict,
        openTimes=openTimes,
        preview=False,
        newActivity=newActivity,
        active="listing",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# Event listing page

@app.route('/event-listing/<title>')
def event_listing_page(title):
    """
    Constructs url using <title> passed to it. Takes the event_id also passed to it and pulls
    the relevant event from the database. All the data is then passed to the 
    template as it renders to display the event listing in the browser. 
    """
    loggedIn = True if 'user' in session else False

    event_id = request.args.get('event_id')
    newEvent = request.args.get('newEvent')

    event = db.events.find_one({"_id": ObjectId(event_id)})
    date = event['date'].strftime("%d %b %Y")
    rawDescrip = event['description']
    descrpDict = Helpers.format_description(rawDescrip)
    
    return render_template(
        "pages/eventlisting.html", 
        headTitle=title,
        title=title,
        event=event, 
        date=date,
        description=descrpDict,
        newEvent=newEvent,
        loggedIn=loggedIn,
        active="listing",
        keywords=Keywords.generic()
    )

# Settings page
@app.route('/settings/<username>', methods=['GET', 'POST'])
def settings_page(username):
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))

    else: 
        user = db.users.find_one({"username": session['user']})

    if request.method == 'POST':
        post_request = request.get_json()
        response = settings_update(db, user, post_request)
        return json.dumps(response)

    return render_template(
        "pages/settings.html", 
        headTitle="Account Settings", 
        loggedIn=loggedIn,
        active="form",
        keywords=Keywords.generic()
    )

# Account page - all listings for this account
@app.route('/account/<username>')
def my_account_page(username):
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        user = db.users.find_one({"username": session['user']}) 

    return render_template(
        "pages/account.html", 
        headTitle="My Account", 
        loggedIn=loggedIn,
        user=user,
        active="account",
        keywords=Keywords.generic()
    )

# Add new event page
@app.route('/editor/<username>/add-new-event', methods=['GET', 'POST'])
def new_event_page(username):
    """
    Checks if user is logged in, if not redirects to permission denied page.
    Gets user data from the database using the session username. Converts data from form into dict, 
    and sends this to be processed using the process_event_data function, which returns
    the formatted obj. Then obj is inserted into the database.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else: 
        user = db.users.find_one({"username": session['user']})

    if request.method == 'POST':
        post_request = request.form.to_dict()
        published = False
        obj = process_event_data(db, user, post_request, published)
        newEvent_id = db.events.insert_one(obj).inserted_id

        return redirect(url_for(
            'preview_event_page', 
            username=session['user'], 
            title=post_request['title'],
            headTitle="Preview Event",
            event_id=newEvent_id, 
            active="listing",
            new=True))

    return render_template(
        "pages/editor.html", 
        headTitle="Add New Event", 
        editor="new",
        type="event",
        active="form",
        loggedIn=loggedIn,
        keywords=Keywords.generic())

# preview event page
@app.route('/editor/preview-event/<username>/<title>', methods=['GET', 'POST'])
def preview_event_page(username, title):
    """
    Provides a preview of a newly created listing before the user to choose either to edit further or
    publish. Using the event_id the data is pulled from the database, date and description formatted and then 
    passed to the flask to be rendered.
    If user chooses to publish this event the the 'Published' value in the database is set to True. 
    making the listing available to view and search on the site. 
    """
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))

    event_id = request.args.get('event_id')
    event = db.events.find_one({"_id": ObjectId(event_id)})
    date = event['date'].strftime("%d %b %Y")

    rawDescrip = event['description']
    descrpDict = Helpers.format_description(rawDescrip)
    
    published = event['published']
    preview = False if published else True

    headTitle = "Preview | " + title

    if request.method == 'POST':
        db.events.find_one_and_update({"_id": ObjectId(event_id)}, {"$set": {"published": True}})
        return redirect(url_for(
            'event_listing_page', 
            event_id=event_id, 
            title=title, 
            newEvent=True))

    return render_template(
        "pages/eventlisting.html", 
        headTitle=headTitle,
        title=title,
        event=event, 
        date=date,
        description=descrpDict,
        preview=preview,
        loggedIn=loggedIn,
        active="listing",
        keywords=Keywords.generic())

# Edit existing event page
@app.route('/editor/edit-event/<username>/<title>', methods=['GET', 'POST'])
def edit_event_page(username, title):
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        event_id = request.args.get('event_id')
        event = db.events.find_one({"_id": ObjectId(event_id)})
        user = db.users.find_one({'username': session['user']})

        # data to display in edit fields
        date = event['date'].strftime("%d/%m/%Y")
        published = event['published']
        preview = False if published else True
        headTitle = 'Edit | ' + title

    # send data to database when user hits preview
    if request.method == 'POST':
        post_request = request.form.to_dict()
        obj = process_event_data(db, user, post_request, published)
        db.events.find_one_and_update({"_id": ObjectId(event_id)}, {"$set": obj})

        # for loading preview page
        return redirect(url_for(
            'preview_event_page', 
            username=session['user'], 
            title=post_request['title'],
            headTitle="Preview Event",
            active="listing",
            published=published,
            preview=preview, 
            event_id=event_id))

    # for displaying forms when editing
    return render_template(
        "pages/editor.html", 
        headTitle=headTitle, 
        title=title,
        editor="edit",
        type="event",
        event_id=event_id,
        event=event,
        date=date,
        active="form",
        loggedIn=loggedIn,
        keywords=Keywords.generic())

# Add new activity page
@app.route('/editor/<username>/add-new-activity', methods=['GET', 'POST'])
def new_activity_page(username):
    """
    Checks if user is logged in, if not redirects to permission denied page.
    Gets user data from the database using the session username. Converts data from form 
    into dict, then processes into format for database and finally inserts that 
    data into the database.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else: 
        user = db.users.find_one({"username": session['user']})

    if request.method == 'POST':
        post_request = request.form.to_dict()
        published = False
        obj = process_activity_data(db, user, post_request, published)

        newActivity_id = db.activities.insert_one(obj).inserted_id
        
        return redirect(url_for(
            'preview_activity_page', 
            username=session['user'], 
            title=post_request['title'], 
            headTitle="Preview Activity",
            preview=True,
            activity_id=newActivity_id, 
            active="listing",
            new=True
        ))

    return render_template(
        "pages/editor.html", 
        headTitle="Add New Activity", 
        editor="new",
        type="activity",
        active="form",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# preview activity page
@app.route('/editor/preview-activity/<username>/<title>', methods=['GET', 'POST'])
def preview_activity_page(username, title):
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        activity_id = request.args.get('activity_id')

        activity = db.activities.find_one({"_id": ObjectId(activity_id)})
        startDate = activity["dates"]['start'].strftime("%d %b %Y")
        endDate = activity["dates"]['end'].strftime("%d %b %Y")
        openTimes_db = activity['times']
        rawDescrip = activity['description']

        openTimes = Helpers.open_times(openTimes_db)
        descrpDict = Helpers.format_description(rawDescrip)

    """ If user pushed "Publish" button on preview page, update published to True
        then redirect to actual listing page on site """
    if request.method == 'POST':
        db.activities.find_one_and_update({"_id": ObjectId(activity_id)}, {"$set": {"published": True}})
        
        return redirect(url_for(
            'activity_listing_page', 
            activity_id=activity_id, 
            title=title, 
            newActivity=True 
        ))

    return render_template(
        "pages/activitylisting.html", 
        headTitle="Preview Activity",
        title=title, 
        activity=activity,
        startDate=startDate,
        endDate=endDate,
        description=descrpDict,
        openTimes=openTimes,
        preview=True,
        loggedIn=loggedIn,
        active="listing",
        keywords=Keywords.generic()
    )

# Edit existing activity page
@app.route('/editor/edit-activity/<username>/<title>', methods=['GET', 'POST'])
def edit_activity_page(username, title):
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        activity_id = request.args.get('activity_id')
        activity = db.activities.find_one({"_id": ObjectId(activity_id)})
        user = db.users.find_one({"username": session['user']})

        # data to display in edit fields
        startDate = activity["dates"]['start'].strftime("%d/%m/%Y")
        endDate = activity["dates"]['end'].strftime("%d/%m/%Y")
        openTimes_db = activity['times']
        """ 
        loops through open/close times and converts datetimes for display in browser
        leaves other values as None to make it easier to print out on screen
        """
        openTimes = Helpers.open_times(openTimes_db)
        published = activity['published']
        headTitle = 'Edit | ' + title

        if request.method == 'POST':
            post_request = request.form.to_dict()
            obj = process_activity_data(db, user, post_request, published)
            db.activities.find_one_and_update({"_id": ObjectId(activity_id)}, {"$set": obj})

            # for loading preview page
            return redirect(url_for(
                'preview_activity_page', 
                username=session['user'], 
                title=post_request['title'], 
                headTitle="Preview Activity",
                active="listing",
                preview=True,
                published=published,
                activity_id=activity_id
            ))

    # for displaying forms when editing
    return render_template(
        "pages/editor.html", 
        headTitle=headTitle, 
        title=title,
        editor="edit",
        type="activity",
        activity_id=activity_id,
        activity=activity,
        startDate=startDate,
        endDate=endDate,
        openTimes=openTimes,
        active="form",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

# No permission page
@app.route('/permission-denied')
def permission_denied():
    return render_template("pages/permission.html")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
