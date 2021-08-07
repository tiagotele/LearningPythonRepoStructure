import unittest
from unittest.mock import patch
from request.ClassWithRequest import ClassWithRequest

class TestRequestExample(unittest.TestCase):
	
	def test_get_id(self):
		obj = ClassWithRequest()

		with patch('request.ClassWithRequest.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text='Success'

			id=6
			url=f'http://company.com/{id}'
			result=obj.get_from_url(id)
			mocked_get.assert_called_with(url)
			self.assertEqual(result,'Success')
