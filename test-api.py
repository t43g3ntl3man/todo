import unittest
from todo import todo


import unittest

from app import app
app.testing = True

class testApi(unittest.TestCase):
	def test_main(self):
		sent = {'id':todoCount + 1, 'title':'test', 'description': 'description', 'done':0}
		result = client.post('/todo/api/v1.0/tasks', data=sent)
		self.assertEqual(
		result.data,
		json.dumps(sent)
		)
