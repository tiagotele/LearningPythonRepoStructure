from .rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

	def test_rectangle_area(self):
		expected_area = 12
		width = 3
		length = 4
		r = Rectangle(width,length)
		self.assertEqual(r.area(), expected_area)
