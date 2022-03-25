"""Entered on the index page as a post for show_summary
def test_login_refused(client):
    response = client.post('/showSummary', data={'email': 'inexistant@email.com'})
    data = response.data.decode()
    assert "Email was not found. Please try again." in response.data.decode()

"""
import pytest
from http import HTTPStatus
from conftest import client

def test__status_code__ok(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert b'GUDLFT Registration' in response.data
    assert b'Welcome to the GUDLFT Registration Portal!' \
        in response.data
    assert b'Please enter your secretary email to continue:' \
        in response.data

"""   
def test_login_with_wrong_email(client):
    response = client.post('/showSummary', data={'email': 'inexistant@mail.com'}, follow_redirects=True)
    data = response.data.decode()
    #  assert response.status_code == 200
    assert "Email is invalid. Please try again." in data

test_login_with_wrong_email(client=client)
"""

def test_book_place
    # enough points
    # not enough points

def test_book_more_than_12_places
    # refusal

def test_book_past_comp
    # refusal

def test_book_full_comp
    # refusal

def test_points_update
    # when booking the points of the club should be substracted

def test_comp_place_substracted
    # when booking the number of place should be substracted by the number of places booked in the last request

