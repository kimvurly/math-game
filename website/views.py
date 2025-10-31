# standard routes for the website, where users can actually go, not authentication
from flask import Blueprint, render_template, request, render_template, redirect, url_for # blueprint of our website, has a bunch of routes
import random

views = Blueprint('views', __name__) # sets up blueprint

# function will run whenever we go to the main page of the website
@views.route('/') # decorator
def home():
    return render_template("index.html")

@views.route('/addition')
def addition():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    problem = f"{a} + {b}"
    answer = a + b
    
    return render_template("addition.html", problem=problem, answer=answer)

@views.route('/subtraction')
def subtraction():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    problem = f"{a} - {b}"
    answer = a - b

    return render_template("subtraction.html", problem=problem, answer=answer)

@views.route('/multiplication')
def multiplication():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    problem = f"{a} x {b}"
    answer = a*b

    return render_template("multiplication.html")