"""This test the homepage"""

def test_request_landing_page(client):
    """Calls the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Email" in response.data

def test_request_page_not_found(client):
    """Calls a fake page"""
    response = client.get("/xxxxx")
    assert response.status_code == 404

def test_request_index_page(client):
    """Tests main page is inaccessible when not logged in"""
    response = client.get("/main", follow_redirects=False)
    assert response.status_code == 302

    '''Tests that unauthenticated users are redirected to Login page'''
    response = client.get('/main', follow_redirects=True)
    assert response.status_code == 200
    assert b"Email" in response.data
