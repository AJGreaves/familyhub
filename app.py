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
def events_page():
    return render_template("contact.html", title="Contact", active="contact")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)