import pytest
import server


def mock_clubs():
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
        {"name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]
    return clubs


def mock_competitions():
    comps = [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
    return comps


@pytest.fixture
def mock_data(mocker):
    mocker.patch.object(server, 'clubs', mock_clubs())
    mocker.patch.object(server, 'competitions', mock_competitions())
    return mocker
