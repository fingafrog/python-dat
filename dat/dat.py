import requests

class Dat:
    login_url = 'https://rateview.dat.com/api/session/login'
    locations_url = 'https://rateview.dat.com/api/location/suggestions'
    historicals_url = 'https://rateview.dat.com/api/search/getRateSearch'
    rate_market = 'Spot'
    rate_type = 'PerTrip'

class Session(Dat):
    def __init__(self, token):
        self.session = requests.session()
        self.token = token
        self.connect()

    def connect(self):
        """Create session with Dat Rateview via http."""
        self.session.post(self.login_url, data=self.token)
