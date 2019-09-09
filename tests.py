import unittest
import requests
import dat
import os


class TestDatCase(unittest.TestCase):
    def setUp(self):
        self.username = os.environ['DAT_USERNAME']
        self.password = os.environ['DAT_PASSWORD']

    def tearDown(self):
        pass

    def test_connect(self):
        s = dat.connect(self.username, self.password)
        self.assertTrue('.TCAUTH' in s.cookies.get_dict())


if __name__ == '__main__':
    unittest.main(verbosity=2)
