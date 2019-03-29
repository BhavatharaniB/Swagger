# import required packages
import unittest
import requests
import json


class Test(unittest.TestCase):

    def setUp(self):
        self.data = {"message": "hey"}
        self.data1 = {{"message": "hey", "message": "hey_all"}}
        self.header = {'content-type': 'application/json'}
        self.cdata = json.dumps(self.data)
        self.cdata1 = json.dumps(self.data1)

    def tearDown(self):
        pass

    # testing get method
    def test_success_get(self):
        resp = requests.get(url="http://127.0.0.1:5000/get_details?name={}".format("Hello"))
        x = resp.json()
        y = x.get('data').get('message')
        self.assertEqual(y, "Hello")

    # testing post method
    def test_success_post(self):
        resp = requests.post(url="http://127.0.0.1:5000/post", headers=self.header, data=self.cdata)
        self.assertEqual(resp.status_code, 200)

    # testing put method
    def test_success_put(self):
        resp = requests.put(url="http://127.0.0.1:5000/put", headers=self.header, data=self.cdata1)
        self.assertEqual(resp.status_code, 200)

    # testing delete method
    def test_success_delete(self):
        resp = requests.delete(url="http://127.0.0.1:5000/delete", headers=self.header, data=self.cdata)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
