# standard routes for the website, where users can actually go, not authentication
from flask import Blueprint, render_template # blueprint of our website, has a bunch of routes

views = Blueprint('views', __name__) # sets up blueprint

# function will run whenever we go to the main page of the website
@views.route('/') # decorator
def home():
    return render_template("index.html")

@views.route('/addition')
def addition():
    return render_template("addition.html")

@views.route('/subtraction')
def subtraction():
    return render_template("subtraction.html")
