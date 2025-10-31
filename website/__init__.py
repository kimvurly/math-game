from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # initializing flask
    app = Flask(__name__)
    # encrypt and secure the cookies and session data
    app.config['SECRET_KEY'] = 'kimberly vu is so awesome sauce yay'

    # registering blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app