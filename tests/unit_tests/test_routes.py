import pytest


'''Test the publicly accessible route for points display'''
def test_rankings_route(client):
    response = client.get('/rankings')
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Club name' in response_data
    assert 'Simply Lift' in response_data


"""We will here test for the routes"""
def test_index_route(client):
    response = client.get('/')
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Registration' in response_data
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response_data


"""test to logout, response == 200 and data exists"""
def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 200
    assert 'disconnected' in response.data.decode()


"""test to purchase place with true data"""
def test_purchase_places(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 1})
    assert response.status_code == 200
    assert 'complete' in response.data.decode()


def test_can_not_purchase_places_old_comp(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1})
    assert response.status_code == 200
    assert 'past competition' in response.data.decode()


def test_purchase_too_much_places(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 26})
    assert response.status_code == 200
    assert 'maximum of 12' in response.data.decode()


def test_purchase_not_enought_points(client):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 6})
    assert response.status_code == 200
    assert 'does not have enough points' in response.data.decode()


"""test to show summary with wrong data"""
def test_show_summary(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert 'Welcome' in response.data.decode()
    assert 'Points available' in response.data.decode()


"""Fail to log in due to wrong email"""
def test_fail_show_summary(client):
    email = 'wrong@inexistant.com'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200
    assert 'Email was not found' in response.data.decode()


"""test to book/comp/club with true data"""
def test_book(client):
    response = client.get('/book/' + "Spring Festival"+"/Simply Lift")
    assert response.status_code == 200
    assert "Here is the form to complete" in response.data.decode()
