"""This test the main menu"""
import os

from flask import request
from werkzeug.security import generate_password_hash

from app import db
from app.db.models import User


user = User('abc@test.com', generate_password_hash('test1234'))
data = {'email': 'abc@test.com', 'password': 'test1234'}

def test_request_main_menu_links(client):
    """Calls the index page but will redirect to main login if not authenticated"""
    response = client.get("/main")
    assert response.status_code == 200
    assert b"Email" in response.data


def test_request_main_menu_links_authenticated(client, application):
    '''Tests user registration'''
    # Test starts assuming there is no user in db
    assert db.session.query(User).count() == 0
    with application.app_context():
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        response = client.post('/main', data=data, follow_redirects=True)
        assert response.status_code == 200
        assert b"Dashboard" in response.data
        assert b"Transactions" in response.data
        assert b"Logs" in response.data
        db.session.delete(user)
        db.session.commit()
        assert db.session.query(User).count() == 0


# def test_loggedin_upload_access(client, application):
#     '''Tests access to upload page when logged in'''
#
#     # Loads user for login - this persists through rest of testing in this file
#     @application.login_manager.request_loader
#     def load_user_from_request(request):
#         return User.query.first()
#
#     response = client.get('/transactions_browse/upload')
#     assert response.status_code == 200
#     assert b"Upload" in response.data
#     db.session.delete(user)
#     db.session.commit()
#     assert db.session.query(User).count() == 0

