from flask import Blueprint, render_template, request, url_for, redirect

auth = Blueprint('auth', __name__)

@auth.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method =='POST':
        button = request.form['submit_button']
        if button == "enter_addition":
            # check if answer is right.
                # go to /subtraction
            # else
                # display /wrong screen (figure out how to do popup)
            url = url_for('views.addition')
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)

@auth.route('/subtraction', methods=['GET', 'POST'])
def subtraction():
    if request.method =='POST':
        button = request.form['submit_button']
        if button == "enter_subtraction":
            # check if answer is right.
                # go to /subtraction
            # else
                # display /wrong screen (figure out how to do popup)
            url = url_for("views.subtraction")
        elif button == "exit_button":
            # return to main page
            url = url_for('views.home')
    return redirect(url)