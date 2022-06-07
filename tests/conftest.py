import pytest
from server import app, load_clubs, load_competitions



@pytest.fixture
def client():
    """ Allows the testing to be launched and under the Testing parameter"""
    client = app.test_client()
    return client


def mock_load_competitions():
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Back to the Future",
            "date": "2985-10-26 00:00:00",
            "numberOfPlaces": "13"
        }
    ]
    return competitions


def mock_load_clubs():
    clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "500"
        }
    ]
    return clubs


@pytest.fixture
def mock_competitions_and_clubs(mocker):
    mocker.patch.object(server, 'competitions', mock_load_competitions())
    mocker.patch.object(server, 'clubs', mock_load_clubs())
    return mocker
