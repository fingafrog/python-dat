import requests
import pandas as pd

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
        """create session with Dat Rateview via http"""
        self.session.post(self.login_url, data=self.token)

class Helper(Session):
    def search_locations(self, search_str):
        """Return json for search_str ('city, state, zip') to get location id
        using Dat to find best match."""
        payload = {'term': search_str}
        return self.session.post(self.locations_url, json=payload).json()

    def search_historicals(self, origin_id, dest_id, equipment='Dry'):
        payload = {
            'rateMarket': self.rate_market,
            'rateType': self.rate_type,
            'equipmentCategory': equipment,
            'originHandle': origin_id,
            'destinationHandle': dest_id
           }
        return self.session.post(self.historicals_url, json=payload).json()

    def search(self, origin_str, dest_str):
        """using search_str ('city, state, zip') get json of historical data
        from Dat"""
        origin_id = self.search_locations(origin_str)[0]['handle']
        dest_id = self.search_locations(dest_str)[0]['handle']
        return self.search_historicals(origin_id, dest_id)
