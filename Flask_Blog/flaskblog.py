from flask import Flask, render_template
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__, '/static') #flask needs to know where files are

mongo = MongoClient(port = 27017)

db = mongo.music

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/newyork")
def newyork():
    return render_template('newyork.html')

@app.route("/losangeles")
def losangeles():
    return render_template('losangeles.html')

@app.route("/atlanta")
def atlanta():
    return render_template('atlanta.html')

@app.route("/dc")
def dc():
    return (render_template('dc1.html'))


@app.route("/nashville")
def nashville():
    return render_template('nashville.html')

@app.route("/austin")
def austin():
    return render_template('austinFix.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run() #do we need this?