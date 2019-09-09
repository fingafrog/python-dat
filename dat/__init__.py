import requests

class Dat:
    login_url = 'https://rateview.dat.com/api/session/login'
    locations_url = 'https://rateview.dat.com/api/location/suggestions'
    historicals_url = 'https://rateview.dat.com/api/search/getRateSearch'

def connect(username, password):
    """create session with Dat Rateview via http"""
    s = requests.session()
    token = {'userName': username, 'password': password}
    s.post(Dat.login_url, data=token)
    return s
