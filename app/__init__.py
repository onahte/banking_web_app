"""A simple flask web app"""
import os
import flask_login
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

from .cli import create_database, create_logs
from .db import database, db
from .db.models import User
from .simple_pages import simple_pages
from .error_handlers import error_handlers
from .auth import auth
from .transactions import transactions
from .context_processors import utility_text_processors
from .error_handlers import error_handlers
from .logging_config import log_con
from .static import images

login_manager = flask_login.LoginManager()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    if os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("app.config.TestingConfig")

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)

    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.register_blueprint(transactions)
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.register_blueprint(database)
    app.context_processor(utility_text_processors)

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
