import pytest
import server

@pytest.fixture
def client():
    """ Allows the testing to be launched and under the Testing parameter"""
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    return client
