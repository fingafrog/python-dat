import unittest
import requests
from dat import Helper
import os


class TestDatCase(unittest.TestCase):
    def setUp(self):
        self.username = os.environ['DAT_USERNAME']
        self.password = os.environ['DAT_PASSWORD']

    def tearDown(self):
        pass

    def test_connect(self):
        token = {'userName': self.username, 'password': self.password}
        helper = Helper(token)
        self.assertTrue('.TCAUTH' in helper.session.cookies.get_dict())

    def test_search_locations(self):
        token = {'userName': self.username, 'password': self.password}
        session = Helper(token)
        location = 'Cherry Hill, NJ, 08002'
        location_data = session.get_location(location)
        self.assertTrue('handle' in location_data[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
