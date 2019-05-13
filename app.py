import os
from flask import Flask, flash, render_template, redirect, request, url_for, session, abort, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone-3-festivals'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-gdxlz.mongodb.net/milestone-3-festivals?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
def get_index():
    return render_template('index.html')
    
@app.route('/view_festivals')
def view_festivals():
    return render_template('festivals.html')
    
@app.route('/add_festival')
def add_festival():
    return render_template('addfestival.html')
    
@app.route('/insert_festival', methods=['POST'])
def insert_festival():
    festivals = mongo.db.festivals
    festivals.insert_one(request.form.to_dict())
    return redirect(url_for('thanks'))
    
@app.route('/thanks')
def thanks():
    return render_template('thankyou.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
