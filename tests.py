import unittest
import requests
from dat.helpers import PandasWrapper
import os


class DatHelperCase(unittest.TestCase):
    def setUp(self):
        self.username = os.environ['DAT_USERNAME']
        self.password = os.environ['DAT_PASSWORD']
        self.token = {'userName': self.username, 'password': self.password}

    def tearDown(self):
        pass

    def test_connect(self):
        helper = PandasWrapper(self.token)
        self.assertTrue('.TCAUTH' in helper.session.cookies.get_dict())

    def test_helper_components(self):

        # basic Dat location handle search
        helper = PandasWrapper(self.token)
        origin = 'Cherry Hill, NJ, 08002'
        origin_data = helper.search_locations(origin)
        self.assertTrue('handle' in origin_data[0])

        # basic Dat lane historicals json search
        origin_id = origin_data[0]['handle']
        dest = 'Philadelphia, PA, 19106'
        dest_id = helper.search_locations(dest)[0]['handle']
        historical_json = helper.search_historicals(origin_id, dest_id)
        self.assertTrue('result' in historical_json)

        # convert Dat lane historicals json to Pandas Dataframe
        df = helper.historicals_json_to_df(historical_json)
        self.assertTrue(not df.empty)

        # main usage of Dat package via PandasWrapper
        search_results = helper.search(origin, dest)
        self.assertTrue(not search_results.empty)

if __name__ == '__main__':
    unittest.main(verbosity=2)
