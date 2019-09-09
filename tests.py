import unittest
import requests
from dat import Helper
import os


class TestDatCase(unittest.TestCase):
    def setUp(self):
        self.username = os.environ['DAT_USERNAME']
        self.password = os.environ['DAT_PASSWORD']
        self.token = {'userName': self.username, 'password': self.password}

    def tearDown(self):
        pass

    def test_connect(self):
        helper = Helper(self.token)
        self.assertTrue('.TCAUTH' in helper.session.cookies.get_dict())

    def test_search_locations(self):
        helper = Helper(self.token)
        location = 'Cherry Hill, NJ, 08002'
        location_data = helper.search_locations(location)
        self.assertTrue('handle' in location_data[0])

    def test_search_historicals(self):
        helper = Helper(self.token)
        origin = 'Cherry Hill, NJ, 08002'
        dest = 'Cherry Hill, NJ, 08002'
        origin_id = helper.search_locations(origin)[0]['handle']
        dest_id = helper.search_locations(dest)[0]['handle']
        historical_data = helper.search_historicals(origin_id, dest_id)
        self.assertTrue('result' in historical_data)

    def test_search(self):
        helper = Helper(self.token)
        origin = 'Cherry Hill, NJ, 08002'
        dest = 'Cherry Hill, NJ, 08002'
        historical_data = helper.search(origin, dest)
        self.assertTrue('result' in historical_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
