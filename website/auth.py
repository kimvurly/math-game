from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/swiping', methods=['GET', 'POST'])
def swiping():
    return