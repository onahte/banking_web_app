"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import os
import pytest

from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, current_user

from app import create_app, db
from app.db.models import User


db = SQLAlchemy()

@pytest.fixture()
def application():
    """This makes the app"""
    #os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_ENV'] = 'testing'
    application = create_app()

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def app_client(application):
    ctx = application.test_request_context()
    ctx.push()
    application.test_client_class = FlaskClient
    return application.test_client()

@pytest.fixture()
def add_user(application):
    with application.app_context():
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        db.session.commit()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()