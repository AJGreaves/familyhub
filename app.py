import os
from flask import Flask

# create instance of flask and assign it to "app"
app = Flask(__name__) 

# create test function as proof of concept
@app.route('/')
def hello():
    return 'Hello World... again!'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)