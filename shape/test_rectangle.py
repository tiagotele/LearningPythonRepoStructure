from shape.rectangle import Rectangle
from random import randrange
import unittest

class TestRectangle(unittest.TestCase):

	def test_rectangle_area(self):
		width = 3.0
		length = 4.0
		expected_area = width * length
		r = Rectangle(width,length)
		self.assertEqual(r.area(), expected_area)

	def test_random_rectangle_area(self):
		width = randrange(100)
		length = randrange(100)
		expected_area = width * length
		r = Rectangle(width,length)
		self.assertEqual(r.area(), expected_area)
	
	@unittest.expectedFailure
	def test_negative_rectangle_area(self):
		width = -3.9
		length = -randrange(100)
		expected_area = width * length
		r = Rectangle(width,length)
		self.assertEqual(r.area(), expected_area)
