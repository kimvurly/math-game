from flask import Blueprint, render_template, request, url_for, redirect, session
import random
import sympy as sp

auth = Blueprint('auth', __name__)

'''
 note for future self: make the code a separate function and js import it
 u can change the very small details with parameters, like the template to render
 and the random problem generation too
'''
@auth.route('/addition', methods=['GET', 'POST'])
def addition():
    # num of questions right to be able to pass onto next level
    required_right = 10
    if 'tries_counter' not in session:
        session['tries_counter'] = 0

    if 'right_counter' not in session:
        session['right_counter'] = 0

    if request.method =='POST':
        button = request.form.get('submit_button')
        answer = int(request.form.get('answer'))
        correct_answer = int(request.form.get('correct_answer'))
        problem = request.form.get('problem')

        if button == "enter_addition":
            if answer == correct_answer:
                session['right_counter'] += 1
                # make them answer a certain number of questions to move on
                if session['right_counter'] >= required_right:
                    # reset all session things
                    session['tries_counter'] = 0
                    session['right_counter'] = 0
                    # go to /subtraction if so
                    url = url_for('views.subtraction')
                else:
                    # reset tries counter (just in case im paranoid) and generate new problem
                    session['tries_counter'] = 0
                    url = url_for('views.addition')
            else:
                if session['tries_counter'] < 3:
                    error = f"wrong! you have {3 - session['tries_counter']} tries left."
                    session['tries_counter'] += 1
                    return render_template("addition.html", problem=problem, answer=correct_answer, error=error)
                elif session['tries_counter'] == 3:
                    # display error
                    error = f"sorry, the answer is {correct_answer}."
                    # reset counter for next problem
                    session['tries_counter'] = 0
                    # generate new problem and answer
                    a = random.randint(1, 20)
                    b = random.randint(1, 20)
                    problem = f"{a} + {b}"
                    new_answer = a + b
                    return render_template("addition.html", problem=problem, answer=new_answer, error=error)
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)

@auth.route('/subtraction', methods=['GET', 'POST'])
def subtraction():
    required_right = 10
    if 'tries_counter' not in session:
        session['tries_counter'] = 0
    
    if 'right_counter' not in session:
        session['right_counter'] = 0

    if request.method =='POST':
        button = request.form.get('submit_button')
        answer = int(request.form.get('answer'))
        correct_answer = int(request.form.get('correct_answer'))
        problem = request.form.get('problem')

        if button == "enter_subtraction":
            # check if answer is right.
            if answer == correct_answer:
                session['right_counter'] += 1
                # make them answer a certain number of questions to move on
                if session['right_counter'] >= required_right:
                    # reset all session things
                    session['tries_counter'] = 0
                    session['right_counter'] = 0
                    # go to /multiplication
                    url = url_for('views.multiplication')
                else:
                    # reset tries counter
                    session['tries_counter'] = 0
                    url = url_for('views.subtraction')
            else:
                # let the user try the problem 4 times
                if session['tries_counter'] < 3:
                    # display number of tries left each time
                    error = f"wrong! you have {3 - session['tries_counter']} tries left."
                    session['tries_counter'] += 1
                    return render_template("subtraction.html", problem=problem, answer=correct_answer, error=error)
                # if at 4 tries, just display the right answer
                elif session['tries_counter'] == 3:
                    error = f"sorry, the answer is {correct_answer}."
                    # reset counter for next problem (again, paranoid)
                    session['tries_counter'] = 0
                    # generate new problem and answer
                    a = random.randint(1, 100)
                    b = random.randint(1, 100)
                    problem = f"{a} - {b}"
                    new_answer = a - b
                    return render_template("subtraction.html", problem=problem, answer=new_answer, error=error)
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)

@auth.route('/multiplication', methods=['GET', 'POST'])
def multiplication():
    required_right = 10
    if 'tries_counter' not in session:
        session['tries_counter'] = 0

    if 'right_counter' not in session:
        session['right_counter'] = 0
    
    if request.method == 'POST':
        button = request.form.get('submit_button')
        answer = int(request.form.get('answer'))
        correct_answer = int(request.form.get('correct_answer'))
        problem = request.form.get('problem')

        if button == "enter_multiplication":
            # check if answer is right
            if answer == correct_answer:
                session['right_counter'] += 1
                # make them answer a certain number of questions to pass
                if session['right_counter'] >= required_right:
                    # reset all session things
                    session['tries_counter'] = 0
                    session['right_counter'] = 0

                    # go to /division
                    url = url_for('views.division')
                else:
                    # reset tries counter
                    session['tries_counter'] = 0
                    url = url_for('views.subtraction')
            else:
                # let the user try the problem 4 times
                if session['tries_counter'] < 3:
                    # display number of tries left each time
                    error = f"wrong! you have {3 - session['tries_counter']} tries left."
                    session['tries_counter'] += 1
                # if at 4 tries, display right answer
                elif session['tries_counter'] == 3:
                    error = f"sorry, the answer is {correct_answer}."
                    # reset counter for next problem
                    session['tries_counter'] = 0
                    # generate new problem and answer
                    a = random.randint(1, 100)
                    b = random.randint(1, 100)
                    problem = f"{a} x {b}"
                    new_answer = a*b
                    return render_template("multiplication.html", problem=problem, answer=new_answer, error=error)
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)

@auth.route('/division', methods=['GET', 'POST'])
def division():
    required_right = 10
    if 'tries_counter' not in session:
        session['tries_counter'] = 0

    if 'right_counter' not in session:
        session['right_counter'] = 0
    
    if request.method == 'POST':
        button = request.form.get('submit_button')
        answer = int(request.form.get('answer'))
        correct_answer = int(request.form.get('correct_answer'))
        problem = request.form.get('problem')

        if button == "enter_division":
            # check if answer is right
            if answer == correct_answer:
                session['right_counter'] += 1
                # make them answer a certain number of questions to pass
                if session['right_counter'] >= required_right:
                    # reset all session things
                    session['tries_counter'] = 0
                    session['right_counter'] = 0

                    # go to end or maybe try doing algebra problems?
                    url = url_for('views.algebra')
                else:
                    # reset tries counter
                    session['tries_counter'] = 0
                    url = url_for('views.subtraction')
            else:
                # let the user try the problem 4 times
                if session['tries_counter'] < 3:
                    # display number of tries left each time
                    error = f"wrong! you have {3 - session['tries_counter']} tries left."
                    session['tries_counter'] += 1
                # if at 4 tries, display right answer
                    if session['tries_counter'] == 3:
                        error =f"sorry, the answer is {correct_answer}."
                        # reset counter for next problem
                        session['tries_counter'] = 0
                        # generate new problem and number
                        a = random.randint(1, 100)
                        b = a*random.randint(1, 100)
                        problem = f"{b} / {a}"
                        new_answer = b/a

                        return render_template("division.html", problem=problem, answer=new_answer, error=error)
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)

@auth.route('/algebra', methods=['GET', 'POST'])
def algebra():
    required_right = 2
    if 'tries_counter' not in session:
        session['tries_counter'] = 0

    if 'right_counter' not in session:
        session['right_counter'] = 0

    if request.method == 'POST':
        button = request.form.get('submit_button')
        answer = request.form.get('answer')
        correct_answer = request.form.get('correct_answer')
        problem = request.form.get('problem')

        if button =="enter_algebra_1":
            # check if answer is right
            if answer == correct_answer:
                session['right_counter'] += 1
                # make them answer a certain number of questions
                if session['right_counter'] == required_right:
                    # reset all session things
                    session['tries_counter'] = 0
                    session['right_counter'] = 0

                    # go to next algebra level (quadratics)
                    url = url_for('views.algebra')
                else:
                    # reset tries counter
                    session['tries_counter'] = 0
                    url = url_for('views.algebra') # change later

            else:
                # let the user try the problem 4 times
                if session['tries_counter'] < 3:
                    error = f"wrong! you have {3 - session['tries_counter']} tries left."
                    session['tries_counter'] += 1
                # if at 4 tries, display right answer
                    if session['tries_counter'] == 3:
                        error = f"sorry, the answer is {correct_answer}."
                        # reset counter for next problem
                        session['tries_counter'] = 0
                        # generate new problem and number
                        a = random.randint(1, 20)
                        b = random.randint(1, 20)
                        c = random.randint(1, 20)
                        x= symbols('x')
                        equation = Eq(a*x + b, c)
                        problem = f"{a}x + {b} = {c}"
                        new_answer = solve(equation, x)[0]

                        return render_template("algebra.html", problem=problem, answer=new_answer, error=error)
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)
