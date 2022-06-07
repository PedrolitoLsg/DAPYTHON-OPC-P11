from server import app
import pytest


@pytest.fixture
def client():
    """ Allows the testing to be launched and under the Testing parameter"""
    client = app.test_client()
    return client


@pytest.mark.usefixtures("client")
class Tests:

    """We will here test for the routes"""
    def test_index_route(self, client):
        response = client.get('/')
        response_data = response.data.decode()
        assert response.status_code == 200
        assert 'Registration' in response_data
        assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response_data



    '''Test the publicly accessible route for points display'''
    """
    def test_rankings_route():
        app = Flask(__name__)
        configure_routes(app)
        client = app.test_client()
        response = client.get('/rankings')
        response_data = response.data.decode()
        assert response.status_code == 200
        assert 'Club name' in response_data
        assert 'Simply Lift' in response_data
    """




    """test to logout, response == 200 and data exists"""
    def test_logout(self, client):
        response = client.get('/logout')
        assert response.status_code == 200
        assert 'disconnected' in response.data.decode()


    """test to purchase place with true data"""
    def test_purchase_places(self, client):
        response = client.post('/purchaseplaces', data={'club': 'Simply Lift',
                                                        'competition': 'Spring Festival', 'places': '1'
                                                        }
                               )
        assert response.status_code == 200
        assert 'complete' in response.data.decode()


    def test_can_not_purchase_places_old_comp(self, client):
        response = client.post('/purchaseplaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1})
        assert response.status_code == 200
        assert 'past competition' in response.data.decode()


    def test_purchase_too_much_places(self, client):
        response = client.post('/purchaseplaces', data={'club': 'She Lifts',
                                                        'competition': 'Spring Festival', 'places': 13
                                                        }
                               )
        assert response.status_code == 200
        assert 'book a maximum' in response.data.decode()


    def test_purchase_not_enought_points(self, client):
        response = client.post('/purchaseplaces', data={'club': 'Simply Lift',
                                                        'competition': 'Spring Festival',
                                                        'places': 6
                                                        }
                               )
        assert response.status_code == 200
        assert 'does not have enough points' in response.data.decode()


    """test to show summary with wrong data"""
    def test_show_summary(self, client):
        response = client.post('/showsummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200
        assert 'Welcome' in response.data.decode()
        assert 'Points available' in response.data.decode()


    """Fail to log in due to wrong email"""
    def test_fail_show_summary(self, client):
        email = 'wrong@inexistant.com'
        response = client.post('/showsummary', data={'email': email})
        assert response.status_code == 200
        assert 'Email was not found' in response.data.decode()