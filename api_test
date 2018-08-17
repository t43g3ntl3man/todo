import unittest, json
from todo import todo

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] =True
        self.app=app.test_client()

    def tearDown(self):
        pass

    def test_api_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

unittest.main()
