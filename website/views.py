# standard routes for the website, where users can actually go, not authentication
from flask import Blueprint, render_template, request, render_template, redirect, url_for # blueprint of our website, has a bunch of routes
import random
from sympy import symbols, Eq, solve

views = Blueprint('views', __name__) # sets up blueprint

# function will run whenever we go to the main page of the website
@views.route('/') # decorator
def home():
    return render_template("index.html")

@views.route('/addition')
def addition():
    a = random.randint(10, 100)
    b = random.randint(10, 100)
    problem = f"{a} + {b}"
    answer = a + b
    
    return render_template("addition.html", problem=problem, answer=answer)

@views.route('/subtraction')
def subtraction():
    a = random.randint(10, 100)
    b = random.randint(10, 100)
    problem = f"{a} - {b}"
    answer = a - b

    return render_template("subtraction.html", problem=problem, answer=answer)

@views.route('/multiplication')
def multiplication():
    a = random.randint(2, 100)
    b = random.randint(2, 100)
    problem = f"{a} x {b}"
    answer = a*b

    return render_template("multiplication.html", problem=problem, answer=answer)

@views.route('/division')
def division():
    a = random.randint(2, 100)
    b = a * random.randint(1, 100)
    problem = f"{b} / {a}"
    answer = b/a

    return render_template("division.html", problem=problem, answer=answer)

@views.route('/algebra')
def algebra():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    x= symbols('x')
    equation = Eq(a*x + b, c)
    problem = f"{a}x + {b} = {c}"
    answer = solve(equation, x)[0]
    
    return render_template("algebra.html", problem=problem, answer=answer)