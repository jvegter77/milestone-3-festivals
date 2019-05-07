import os
from flask import Flask, flash, render_template, redirect, request, url_for, session, abort, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone-3-festivals'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-gdxlz.mongodb.net/milestone-3-festivals?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'Hello World...again'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
