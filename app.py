import os, json
from flask import Flask, redirect, render_template, request, url_for, jsonify, session
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from familyhubapp.keys import Keywords
from datetime import datetime

# create instance of flask and assign it to "app"
app = Flask(__name__)
app.config.from_object(Config)

# MongoDB URI / Assign db
client = MongoClient(Config.MONGO_URI)
db = client.familyHub


# =========================================================================== #

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


# =========================================================================== #

# Activities page
@app.route('/activities')
def activities_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/activities.html", 
                            title="Activities", 
                            active="activities",
                            loggedIn=loggedIn,
                            keywords=Keywords.activities())


# =========================================================================== #

# Events page
@app.route('/events')
def events_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/events.html",
                            title="Events", 
                            active="events",
                            loggedIn=loggedIn,
                            keywords=Keywords.events())


# =========================================================================== #

# Contact page
@app.route('/contact')
def contact_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/contact.html", 
                            title="Contact", 
                            active="contact",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# =========================================================================== #

# new account page

# Takes data collected with fetch in JS, checks if user already exists in the database.
# if they are redirect them to account page
# if they are not then it encrypts the password before sending complete object to mongodb.
# It then returns to JS if the user already existed or not so JS can provide feedback to the user based on that condition.
# page also renders the newaccount page to be viewed

@app.route('/newaccount', methods=['GET', 'POST'])
def new_account_page():
    loggedIn = True if 'user' in session else False

    if loggedIn:
        user_in_db = db.users.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('my_account_page', user=user_in_db['username']))


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


# =========================================================================== #

# login page

# Takes data collected with fetch in JS, checks if user exists in the database
# If the user is in the database it then compares the password provided with the hashed one from the database
# If the password is correct the value of passwordCorrect is set to True
# All this data is then returned to JS to respond accordingly to the browser

@app.route('/login', methods=['GET', 'POST'])
def login_page():

    loggedIn = True if 'user' in session else False

    print(loggedIn)

    if loggedIn == True:
        user_in_db = db.users.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('my_account_page', user=user_in_db['username']))

    if request.method == 'POST':
        post_request = request.get_json()
        
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

        print(username)
        return json.dumps(response)

    return render_template("pages/login.html", 
                            title="Log In", 
                            active="login",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# log out page
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for('home_page'))


# =========================================================================== #

# Search page
@app.route('/search')
def search_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/search.html", 
                            title="Search",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# Activity listing page - see if possible to update this to different routes based on each activity title
@app.route('/activity-listing')
def activity_listing_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/activitylisting.html", 
                            title="Activity Listing",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# Event listing page - see if possible to update this to different routes based on each event title
@app.route('/event-listing')
def event_listing_page():
    loggedIn = True if 'user' in session else False
    return render_template("pages/eventlisting.html", 
                            title="Event Listing",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# Settings page
@app.route('/settings/<username>', methods=['GET', 'POST'])
def settings_page():
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))

    else: 
        user = db.users.find_one({"username": session['user']})

    if request.method == 'POST':

        post_request = request.get_json()

        updated = False

        if post_request['whichForm'] == '#emailEdit':
            if user['email'] == post_request['oldInput']:
                db.users.find_one_and_update({"_id": ObjectId(user["_id"])}, {"$set": {"email": post_request["newInput"]}})
                updated = True
        
        if post_request['whichForm'] == '#passEdit':
            if check_password_hash(user['password'], post_request['oldInput']):
                post_request['newInput'] = generate_password_hash(post_request['newInput'])
                db.users.find_one_and_update({"_id": ObjectId(user["_id"])}, {"$set": {"password": post_request["newInput"]}})
                updated = True

        response = {
            "updated": updated
        }
        return json.dumps(response)

    return render_template("pages/settings.html", 
                            title="Account Settings", 
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# Account page - all listings for this account
@app.route('/account/<username>')
def my_account_page(username):
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        user = db.users.find_one({"username": session['user']}) 

    return render_template("pages/account.html", 
                            title="My Account", 
                            loggedIn=loggedIn,
                            user=user,
                            keywords=Keywords.generic())


# =========================================================================== #

# Add new event page

# Checks if user is logged in, if not redirects to permission denied page.
# Gets user data from the database using the session username.
# Converts data from form into dict, so can be processed before sending to database.
# Processes date information to turn it into format needed to store date in mongodb.
# Processes number string into int for storing correctly.
# creates new object with username from post_request dict, username from databas and
# all boolean values converted as needed to be store correctly in the database,
# and finally inserts that data into the database.

@app.route('/editor/<username>/add-new-event', methods=['GET', 'POST'])
def new_event_page(username):

    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else: 
        user = db.users.find_one({"username": session['user']})

    if request.method == 'POST':

        post_request = request.form.to_dict()

        # credit for date processing code to fellow student Seán Murphy 
        date = post_request['date'].split('/')
        date = f"{date[2]}-{date[1]}-{date[0]}"
        date = datetime.strptime(date, '%Y-%m-%d')

        if post_request.get('from'):
            price_string = post_request.get('from')
            price_int = int(price_string)

        obj = {'username': user['username'], 
                'title': post_request.get('title'),
                'imgUrl': post_request.get('imgUrl'),
                'date': date, 
                'address': {'addressLine1': post_request.get('addressLine1'),
                            'postcode': post_request.get('postcode'),
                            'town': post_request.get('town')},
                'ageRange': {'under4': True if post_request.get('under4') else False,
                            'age4to6': True if post_request.get('age4to6') else False,
                            'age6to8': True if post_request.get('age6to8') else False,
                            'age8to10': True if post_request.get('age8to10') else False,
                            'age10to12': True if post_request.get('age10to12') else False,
                            'age12up': True if post_request.get('age12up') else False},
                'price': {'from': price_int if post_request.get('from') else None,
                            'isFree': True if post_request.get('isFree') else False},
                'indoor': True if post_request.get('indoor') else False,
                'outdoor': True if post_request.get('outdoor') else False,
                'contact': {'url': post_request.get('url'),
                            'email': post_request.get('email'),
                            'facebook': post_request.get('facebook') if post_request.get('facebook') else None,
                            'twitter': post_request.get('twitter') if post_request.get('twitter') else None,
                            'instagram': post_request.get('instagram') if post_request.get('instagram') else None},
                'description': post_request.get('description'),
                'published': False}

        newEvent_id = db.events.insert_one(obj).inserted_id
        return redirect(url_for('preview_event_page', username=session['user'], title=post_request['title'], event_id=newEvent_id, new=True))

    return render_template("pages/editor.html", 
                            title="Add New Event", 
                            editor="new",
                            type="event",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# preview event page
@app.route('/editor/preview-event/<username>/<title>')
def preview_event_page(username, title):
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))

    event_id = request.args.get('event_id')
    new = request.args.get('new')
    event = db.events.find_one({"_id": ObjectId(event_id)})
    date = event['date'].strftime("%d %b %Y")

    rawDescrip = event['description']
    description = (rawDescrip).split('\r\n')
    descripJson = jsonify(description)

    title = "Preview | " + title
    return render_template("pages/eventlisting.html", 
                            title=title,
                            event=event, 
                            date=date,
                            description=descripJson,
                            new=new,
                            preview=True,
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# =========================================================================== #

# Edit existing event page
@app.route('/editor/<username>/edit-event')
def edit_event_page():
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        user = db.users.find_one({"username": session['user']})

    return render_template("pages/editor.html", 
                            title="Edit Event", 
                            editor="edit",
                            type="event",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# Add new activity page

# Checks if user is logged in, if not redirects to permission denied page.
# Gets user data from the database using the session username.
# Converts data from form into dict, so can be processed before sending to database.
# Processes date information to turn it into format needed to store date in mongodb.
# Processes times by first looping through all the possible times, turning them into the correct format for
# mongo and then adding them to a new dict to use to construct the final object to send to mongo.
# creates new object with username from post_request dict, username from database and
# all boolean values converted as needed to be store correctly in the database,
# and finally inserts that data into the database.

@app.route('/editor/<username>/add-new-activity', methods=['GET', 'POST'])
def new_activity_page(username):
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else: 
        user = db.users.find_one({"username": session['user']})

    if request.method == 'POST':

        post_request = request.form.to_dict()

        start = post_request['start'].split('/')
        start = f"{start[2]}-{start[1]}-{start[0]}"
        start = datetime.strptime(start, '%Y-%m-%d')

        end = post_request['end'].split('/')
        end = f"{end[2]}-{end[1]}-{end[0]}"
        end = datetime.strptime(end, '%Y-%m-%d')

        openTimes = ['monStart','monEnd', 'tueStart', 'tueEnd', 
                'wedStart', 'wedEnd', 'thuStart', 'thuEnd',
                'friStart', 'friEnd', 'satStart', 'satEnd',
                'sunStart', 'sunEnd']

        openTimesDict = { }

        for time_name in openTimes:
            if post_request.get(time_name):
                time = time_name
                time = post_request[time].split(':')
                time = f"{time[0]}:{time[1]}:00"
                time = datetime.strptime(time, '%H:%M:%S')
                openTimesDict[time_name] = time

        obj = {'username': user['username'], 
                'title': post_request.get('title'),
                'imgUrl': post_request.get('imgUrl'),
                'dates': { 'start': start, 
                            'end': end },
                'days' : {'mon': True if post_request.get('mon') else False,
                        'tue': True if post_request.get('tue') else False,
                        'wed': True if post_request.get('wed') else False,
                        'thu': True if post_request.get('thu') else False,
                        'fri': True if post_request.get('fri') else False,
                        'sat': True if post_request.get('sat') else False,
                        'sun': True if post_request.get('sun') else False},
                'times': {'monStart': openTimesDict.get('monStart') if openTimesDict.get('monStart') else None,
                        'monEnd': openTimesDict.get('monEnd') if openTimesDict.get('monEnd') else None,
                        'tueStart': openTimesDict.get('tueStart') if openTimesDict.get('tueStart') else None,
                        'tueEnd': openTimesDict.get('tueEnd') if openTimesDict.get('tueEnd') else None,
                        'wedStart': openTimesDict.get('wedStart') if openTimesDict.get('wedStart') else None,
                        'wedEnd': openTimesDict.get('wedEnd') if openTimesDict.get('wedEnd') else None,
                        'thuStart': openTimesDict.get('thuStart') if openTimesDict.get('thuStart') else None,
                        'thuEnd': openTimesDict.get('thuEnd') if openTimesDict.get('thuEnd') else None,
                        'friStart': openTimesDict.get('friStart') if openTimesDict.get('friStart') else None,
                        'friEnd': openTimesDict.get('friEnd') if openTimesDict.get('friEnd') else None,
                        'satStart': openTimesDict.get('satStart') if openTimesDict.get('satStart') else None,
                        'satEnd': openTimesDict.get('satEnd') if openTimesDict.get('satEnd') else None,
                        'sunStart': openTimesDict.get('sunStart') if openTimesDict.get('sunStart') else None,
                        'sunEnd': openTimesDict.get('sunEnd') if openTimesDict.get('sunEnd') else None},
                'address': {'addressLine1': post_request.get('addressLine1'),
                            'postcode': post_request.get('postcode'),
                            'town': post_request.get('town')},
                'ageRange': {'under4': True if post_request.get('under4') else False,
                            'age4to6': True if post_request.get('age4to6') else False,
                            'age6to8': True if post_request.get('age6to8') else False,
                            'age8to10': True if post_request.get('age8to10') else False,
                            'age10to12': True if post_request.get('age10to12') else False,
                            'age12up': True if post_request.get('age12up') else False},
                'indoor': True if post_request.get('indoor') else False,
                'outdoor': True if post_request.get('outdoor') else False,
                'contact': {'url': post_request.get('url'),
                            'email': post_request.get('email'),
                            'facebook': post_request.get('facebook') if post_request.get('facebook') else None,
                            'twitter': post_request.get('twitter') if post_request.get('twitter') else None,
                            'instagram': post_request.get('instagram') if post_request.get('instagram') else None},
                'description': post_request.get('description')}

        db.activities.insert_one(obj)

    return render_template("pages/editor.html", 
                            title="Add New Activity", 
                            editor="new",
                            type="activity",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# preview event page
@app.route('/editor/<username>/preview-activity')
def preview_activity_page():
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))
    else:
        user = db.users.find_one({"username": session['user']})

    return render_template("pages/activitylisting.html", 
                            title="Preview", 
                            preview=True,
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())

# =========================================================================== #

# Edit existing activity page
@app.route('/editor/<username>/edit-activity')
def edit_activity_page():
    
    loggedIn = True if 'user' in session else False

    if not loggedIn:
        return redirect(url_for('permission_denied'))

    return render_template("pages/editor.html", 
                            title="Edit Activity", 
                            editor="edit",
                            type="activity",
                            loggedIn=loggedIn,
                            keywords=Keywords.generic())


# =========================================================================== #

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


# =========================================================================== #

# No permission page
@app.route('/permission-denied')
def permission_denied():
    return render_template("pages/permission.html")


# =========================================================================== #

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), 
            port=os.getenv('PORT'), 
            debug=True)
