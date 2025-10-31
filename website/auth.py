from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method =='POST':
        button = request.form['enter_button']
        if button == "enter_addition":
            # check if answer is right.
                # go to /subtraction
            # else
                # display /wrong screen (figure out how to do popup)
            pass
    return render_template("addition.html")