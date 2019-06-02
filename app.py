from flask import Flask

# create instance of flask and assign it to "app"
app = Flask(__name__) 

# create test function as proof of concept
@app.route('/')
def hello():
    return 'Hello World... again!'

