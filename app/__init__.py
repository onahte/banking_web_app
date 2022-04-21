"""A simple flask web app"""
import os
import flask_login
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from .cli import create_database, create_logs
from .db import db
from .db.models import User
from .simple_pages import simple_pages
from .error_handlers import error_handlers
from .auth import auth
from .context_processors import utility_text_processors

login_manager = flask_login.LoginManager()

def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)
    app.register_blueprint(error_handlers)
    app.register_blueprint(auth)
    app.context_processor(utility_text_processors)
    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(create_logs)

    db.init_app(app)

    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
