from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/template")
def home1():
       return render_template('mangrove_Index.html')