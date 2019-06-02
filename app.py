import os
from flask import Flask, render_template, redirect, request, url_for, request

# create instance of flask and assign it to "app"
app = Flask(__name__) 

# create test function as proof of concept
@app.route('/')
def home_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)