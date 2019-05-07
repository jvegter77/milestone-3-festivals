import os
from flask import Flask, flash, render_template, redirect, request, url_for, session, abort, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World...again'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
