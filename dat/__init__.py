import requests
import pandas as pd

class Dat:
    login_url = 'https://rateview.dat.com/api/session/login'
    locations_url = 'https://rateview.dat.com/api/location/suggestions'
    historicals_url = 'https://rateview.dat.com/api/search/getRateSearch'

class Session(Dat):
    def __init__(self, token):
        self.session = requests.session()
        self.token = token
        self.connect()

    def connect(self):
        """create session with Dat Rateview via http"""
        self.session.post(self.login_url, data=self.token)

class Helper(Session):
    def get_location(self, search_str):
        """Return json for search_str ('city, state, zip') to get location id
        using Dat to find best match."""
        data = {'term': search_str}
        return self.session.post(self.locations_url, json=data).json()
