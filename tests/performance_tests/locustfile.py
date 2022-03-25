from locust import HttpUser, task


"""do the calls of endpoints to check for performance"""
class Test_endpoints(HttpUser):

    @task
    def test_index(self):
        self.client.get('/')


    @task
    def test_summary(self):
        self.client.post('/showSummary', data={'email': 'john@simplylift.co'})


    @task
    def test_book(self):
        self.client.get('/book/Spring Festival/Simply Lift')


    @task
    def test_purchase(self):
        self.client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': '1'})


    @task
    def test_rankings(self):
        self.client.get('/rankings')


    @task
    def test_logout(self):
        self.client.get('/logout')
