import os, json, re
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from familyhubapp.helpers import Helpers
from familyhubapp.forms import new_account_req, login_req, settings_update, process_activity_data
from datetime import datetime

# create instance of flask and assign it to "app"
app = Flask(__name__)
app.config.from_object(Config)

# MongoDB URI / Assign db
client = MongoClient(Config.MONGO_URI)
db = client.familyHub

# custom filter to use in python and jinja
@app.template_filter()
def slugify(text, delim=b'-'):
    """Generates an ASCII-only slug. Credit for this function to http://flask.pocoo.org/snippets/5/"""
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []
    for word in _punct_re.split(text.lower()):
        word = word.encode()
        if word:
            result.append(word)
    string_url = delim.join(result)
    return str(string_url, 'utf-8')

# Home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home_page():
    """
    Creates 3 lists of 12 database entries from featured, sports and 
    summer categoes to display in the 3 carousels on the index page.
    Pulls entry for linneushof from database to display in the TopTip feature box on index page.
    Converts description for toptip feature into shortend version that will print out correctly.
    """
    loggedIn = True if 'user' in session else False

    sports = db.activities.aggregate([{"$match": {"published": True, "categories.sports": True}} , {'$sample': {'size': 12}}])
    sports = list(sports) 
    recommended = db.activities.aggregate([{"$match": {"published": True, "recommended": True}}, {'$sample': {'size': 12}}])
    recommended = list(recommended) 
    summer = db.activities.aggregate([{"$match": {"published": True, "holidays.summer": True}}, {'$sample': {'size': 12}}])
    summer = list(summer) 

    # specific id for linneushof biggest kids park in Benelux
    topTip = db.activities.find_one({"_id": ObjectId('5d0f619e5d80f9fbbe7449f2')})
    rawDescrip = topTip['description']
    topTopDescrp = Helpers.format_description(rawDescrip)
    topTopDescrp = topTopDescrp[0:4]

    return render_template(
        "pages/index.html", 
        headTitle="Home", 
        active="home",
        sports=sports,
        recommended=recommended,
        summer=summer,
        topTip=topTip,
        topTopDescrp=topTopDescrp,
        loggedIn=loggedIn,
        keywords=Keywords.home()
    )

# Activities page
@app.route('/activities', methods=['GET', 'POST'])
def activities_page():
    """
    Receives user input into filters, processes this to return the results from
    MongoDB back to the browser to be displayed.
    """
    loggedIn = True if 'user' in session else False

    if request.method == 'POST':
        post_request = request.get_json()
        location = post_request['location']
        category = post_request['category']
        days = post_request['days']
        inOut = post_request['inOut']
        ageRangeIds = post_request['ageRangeIds']
        otherIds = post_request['otherIds']

        categorySelector = 'categories.' + category

        results = db.activities.find().sort("_id", -1)
        db_request = []

        if len(otherIds) >= 1:
            for otherId in otherIds:
                otherSelector = 'otherDetails.' + otherId
                db_request.append({otherSelector: True})

        if len(ageRangeIds) >= 1:
            for ageRange in ageRangeIds:
                ageSelector = 'ageRange.' + ageRange
                db_request.append({ageSelector: True})

        if inOut != 'either' and inOut != 'both':
            db_request.append({inOut: True})
        elif inOut == 'both':
            db_request.append({'$and': [{'indoor': True}, {'outdoor': True}]})
        
        if days != 'any' and days != 'weekend' and days != 'weekdays':
            daysSelector = 'days.' + days
            db_request.append({daysSelector: True})
        elif days == 'weekend':
            db_request.append({'$or':[{'days.sat': True}, {'days.sun': True}]})
        elif days == 'weekdays':
            db_request.append({'$or': [
                {'days.mon': True}, 
                {'days.tue': True},
                {'days.wed': True},
                {'days.thu': True},
                {'days.fri': True}
            ]})

        if location != 'all':
            db_request.append({'address.town': location})
        if category != 'all':
            db_request.append({categorySelector: True})

        if len(db_request) == 1:
            results = db.activities.find( db_request[0] ).sort("_id", -1)
        elif len(db_request) > 1:
            results = db.activities.find({ '$and': db_request }).sort("_id", -1)

        return dumps(results)

    return render_template(
        "pages/activities.html", 
        headTitle="Activities", 
        active="activities",
        loggedIn=loggedIn,
        keywords=Keywords.activities()
    )

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
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
    """ 
    Checks if user is already logged in, if they are redirects them to their account page.
    If user in not already logged in takes data they added, compares it to check that the 
    user does not already exist in the database, and then returns a response to javascript 
    based on the checks done.
    """
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
    """ 
    Checks if user is already logged in, if they are redirects them to their account page.
    If user in not already logged in takes data they added to log in, compares it to check 
    the users entries of username/email and password match those in the database, if there
    is a match the user is logged in to the site. Then returns a response to javascript 
    based on the checks done so that JS can provide feedback to the user.
    """
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
    """ clears the session of the user which logs them out """
    session.clear()
    return redirect(url_for('home_page'))

# Activity listing page 
@app.route('/listing/<title>', methods=['GET', 'POST'])
def activity_listing_page(title):
    """
    Checks if user is logged in, to display correct navbar configuration.
    gets activity id passed to route with url and pulls that entry from the database
    for display. 
    Processes the data from the database for display and renders it on the page.
    """
    loggedIn = True if 'user' in session else False

    activity_id = request.args.get('activity_id')
    newActivity = request.args.get('newActivity')

    activity = db.activities.find_one({"_id": ObjectId(activity_id)})
    
    startDate = None
    endDate = None
    if activity["dates"]['start']:
        startDate = activity["dates"]['start'].strftime("%d %b %Y")
        endDate = activity["dates"]['end'].strftime("%d %b %Y")

    openTimes_db = activity['times']
    rawDescrip = activity['description']

    openTimes = Helpers.open_times(openTimes_db)
    descrpDict = Helpers.format_description(rawDescrip)

    map_url = Helpers.map_url(activity)

    return render_template(
        "pages/activitylisting.html", 
        headTitle=title,
        title=title,
        activity=activity,
        startDate=startDate,
        endDate=endDate,
        description=descrpDict,
        openTimes=openTimes,
        map_url=map_url,
        preview=False,
        newActivity=newActivity,
        active="listing",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# Settings page
@app.route('/settings/<username>', methods=['GET', 'POST'])
def settings_page(username):
    """
    Checks if user is logged in, if they are not redirects them to the 'permission denied' page. 
    When user makes post request from settings page the data is sent to the settings_update
    function which checks the data input is correct, updates the database if it passes and returns
    a response to JS for feedback to the user.
    """
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
    """
    Checks if user is logged in, if they are not redirects them to the 'permission denied' page. 
    Pulls all users activities from the database to display in their account page.
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        user = db.users.find_one({"username": session['user']})
        activities = db.activities.find({"username": user['username']}).sort("_id", -1)
        activities = list(activities)

    return render_template(
        "pages/account.html", 
        headTitle="My Account", 
        activities=activities,
        loggedIn=loggedIn,
        active="account",
        keywords=Keywords.generic()
    )

# Add new activity page
@app.route('/editor/<username>/add-new', methods=['GET', 'POST'])
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
        title = slugify(post_request['title'])

        newActivity_id = db.activities.insert_one(obj).inserted_id
        
        return redirect(url_for(
            'preview_activity_page', 
            username=session['user'], 
            title=title, 
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
        active="form",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# preview activity page
@app.route('/editor/preview-activity/<username>/<title>', methods=['GET', 'POST'])
def preview_activity_page(username, title):
    """
    Checks if user has permission to be on this page, if not redirects the to permission denied page.
    Takes entry from the database using the activity_id and builds the preview page from the data.
    If user clicks "publish" button adds the entry again with published set to True.
    """ 
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        activity_id = request.args.get('activity_id')

        activity = db.activities.find_one({"_id": ObjectId(activity_id)})
        startDate = None
        endDate = None
        if activity["dates"]['start']:
            startDate = activity["dates"]['start'].strftime("%d %b %Y")
            endDate = activity["dates"]['end'].strftime("%d %b %Y")

        openTimes_db = activity['times']
        rawDescrip = activity['description']

        openTimes = Helpers.open_times(openTimes_db)
        descrpDict = Helpers.format_description(rawDescrip)

    """ 
    If user pushed "Publish" button on preview page, update published to True
    then redirect to actual listing page on site 
    """
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
        headTitle="Preview",
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

# edit existing activity page
@app.route('/editor/edit-activity/<username>/<title>', methods=['GET', 'POST'])
def edit_activity_page(username, title):
    """
    Pulls activity data from database using the id, displays it in the values of the input fields 
    in the edit page. Renders editor page with converted data. 
    """
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        activity_id = request.args.get('activity_id')
        activity = db.activities.find_one({"_id": ObjectId(activity_id)})
        user = db.users.find_one({"username": session['user']})
        title = slugify(activity['title'])

        startDate = None
        endDate = None
        facebook = ""
        instagram = ""
        twitter = ""

        # data to display in edit fields
        imgUrl = Helpers.add_https(activity["imgUrl"])
        url = Helpers.add_https(activity["contact"]["url"])
        if activity["dates"]['start']:
            startDate = activity["dates"]['start'].strftime("%d/%m/%Y")
            endDate = activity["dates"]['end'].strftime("%d/%m/%Y")
        if activity["contact"]["facebook"]:
            facebook = Helpers.add_https(activity["contact"]["facebook"])
        if activity["contact"]["twitter"]:
            twitter = Helpers.add_https(activity["contact"]["twitter"])
        if activity["contact"]["instagram"]:
            instagram = Helpers.add_https(activity["contact"]["instagram"])
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
                title=title, 
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
        imgUrl=imgUrl,
        url=url,
        facebook=facebook,
        twitter=twitter,
        instagram=instagram,
        editor="edit",        
        activity_id=activity_id,
        activity=activity,
        startDate=startDate,
        endDate=endDate,
        openTimes=openTimes,
        active="form",
        loggedIn=loggedIn,
        keywords=Keywords.generic()
    )

# delete listing page
@app.route('/deletelisting', methods=['GET', 'POST'])
def delete_listing():
    """ 
    Checks if user has permission to be on the page, redirects if not. 
    Takes activity_id sent with url and deletes this listing from the database. 
    Then redirects the user back to their my_account_page
    """

    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        activity_id = request.args.get('activity_id')
        user = db.users.find_one({"username": session['user']})
        db.activities.delete_one({"_id": ObjectId(activity_id)})
        activities = db.activities.find({"username": user['username']}) 
    
    return redirect(url_for(
        "my_account_page", 
        username=session['user'],
        activities=activities,
        loggedIn=loggedIn,
        deleted=True
    ))

# privacy policy page
@app.route('/privacy-policy')
def privacy():
    loggedIn = True if 'user' in session else False

    return render_template(
    "pages/privacy.html", 
    headTitle="Privacy Policy", 
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
