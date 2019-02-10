import unittest
import requests
import json

BASE_URL = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'

class TestAssurity(unittest.TestCase):

    resp = requests.get(BASE_URL)

    if resp.status_code != 200:
        raise Exception('GET {}'.format(resp.status_code))

    def test_name(self):
        self.assertEqual(self.resp.json().get('Name'), 'Carbon credits', '"Name" should be "Carbon credits"')

    def test_relist(self):
        self.assertTrue(self.resp.json().get('CanRelist'), '"CanRelist" should be "true"')

    def test_promotions_2x(self):
        #TODO
        print('dummy test')

if __name__ == '__main__':

    print('Running Assurity RESTful API test:')
    unittest.main()