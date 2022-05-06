'''Testing of authenticated user navigation'''
import os

from flask import request
from werkzeug.security import generate_password_hash

from app import db
from app.db.models import User, Transactions


user = User('abc@test.com', generate_password_hash('test1234'), '100')
data = {'email': 'abc@test.com', 'password': 'test1234'}

def test_no_main_menu_access(client):
    """Calls the index page but will redirect to main login if not authenticated"""
    response = client.get("/main")
    assert response.status_code == 200
    assert b"Email" in response.data


def test_no_dashboard_access(client):
    '''Tests dashboard is inaccessible when not logged in'''
    response = client.get('/dashboard', follow_redirects=False)
    assert response.status_code == 302


def test_no_dashboard_access_redirect(client):
    '''Tests that unauthenticated users are redirected to Login page'''
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data


def test_no_upload_access(client):
    '''Tests upload is inaccessible when not logged in'''
    response = client.get('/transactions_browse/upload', follow_redirects=False)
    assert response.status_code == 302


def test_registration(client, application):
    '''Tests user registration'''
    with application.app_context():
        response = client.post('/register', data=data, follow_redirects=True)
        assert response.status_code == 200
        #Successful registration auto routes to login page
        assert b"Login" in response.data


def test_login_and_menu_link_access(client, application):
    '''Tests login and auto navigation to dashboard'''
    #Test user injected into db - this persists through rest of the testing in this file
    with application.app_context():
        db.create_all()
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        response = client.post('/login', data=data, follow_redirects=True)
        assert response.status_code == 200
        #Successful registration routes to dashboard page
        assert b"Welcome" in response.data
        assert b"Dashboard" in response.data
        assert b"Transactions" in response.data
        assert b"Logs" in response.data



def test_loggedin_dashboard_access(client, application):
    '''Tests access to menu links when logged in'''
    #Loads user for login - this persists through rest of testing in this file
    @application.login_manager.request_loader
    def load_user_from_request(request):
        return User.query.first()
    assert db.session.query(User).count() == 1
    response = client.post('/dashboard')
    assert response.status_code == 200
    assert b"Dashboard" in response.data


def test_loggedin_upload_access(client):
    '''Tests access to upload page when logged in'''
    response = client.get('/transactions_browse/upload')
    assert response.status_code == 200
    assert b"Upload" in response.data


# def test_loggedin_dashboard_access(client):
#     '''Tests access to dashboard page when logged in'''
#     response = client.get('/dashboard')
#     assert response.status_code == 200
#     assert b"Dashboard" in response.data


def test_breakdown(client):
    #Breaks down test user and confirms db is empty
    db.session.delete(user)
    db.session.commit()
    assert db.session.query(User).count() == 0
