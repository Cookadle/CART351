#https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify
#jsonify turn python dict in JSON 

#https://www.w3schools.com/python/module_os.asp + https://anomalse.github.io/CART351-Fall-2026/lectures/flask_four.html
#for import os and its many options (for you when you forget)

import json 

import os 

#record when confession made
from datetime import datetime

from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

#filepath setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #__file__ = app.py become anchors
DATA_FILE = os.path.join(BASE_DIR, "data", "confessions.json")

#limit so nobody send giant essay 
MAX_LENGTH = 500

#helper func
#try to docstring each function yea

#https://python.plainenglish.io/how-to-read-json-file-in-python-with-examples-in-2026-9877d0cdca71
#w=write r=read f=file
def load_confessions():
    """Read confessions.json and return python list of confessions"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)  #jsonarray is parse python list
    except (FileNotFoundError, json.JSONDecodeError):
        #fallback file if empty/corrupt no crash 
        return []

def save_confessions(confessions):
    """Write the Python list of confessions back to confessions.json."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        #indent=format //accented letter readable
        json.dump(confessions, f, indent=2, ensure_ascii=False)



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)