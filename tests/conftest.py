import pytest
import server

@pytest.fixture
def client():
    """ Allows the testing to be launched and under the Testing parameter"""
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    yield client


def mock_loadCompetitions():
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


def mock_loadClubs():
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
    mocker.patch.object(server, 'competitions', mock_loadCompetitions())
    mocker.patch.object(server, 'clubs', mock_loadClubs())
