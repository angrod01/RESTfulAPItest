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
        promotions = self.resp.json().get('Promotions')
        for item in promotions:
            if (item.get('Name') == 'Gallery'):
                self.assertTrue('2x larger image' in item.get('Description'), 
                '"Description" should contain "2x larger image" \nDescription:\n' + item.get('Description'))

if __name__ == '__main__':

    print('Running Assurity RESTful API test:')
    unittest.main()