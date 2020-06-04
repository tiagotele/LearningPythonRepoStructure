from .request_example import RequestExample
import unittest


class TestRequestExample(unittest.TestCase):
	
	def test_get_example_url(self):
		re = RequestExample()
		example_content = re.getExample()
		self.assertIsNotNone(example_content)
		self.assertEqual(example_content, "Tiago Melo")
