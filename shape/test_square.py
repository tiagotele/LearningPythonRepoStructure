from .square import Square
from random import randrange
import unittest

class TestSquare(unittest.TestCase):

	def test_single_square_area(self):
		side = 3.0
		expected_area = 9.0
		s = Square(side)
		self.assertEqual(s.area(), expected_area)

	def test_random_side_area(self):
		side = randrange(100)
		expected_area = side*side
		s = Square(side)
		self.assertEqual(s.area(), expected_area)
	

	@unittest.expectedFailure
	def test_negative_side(self):
		side = -3
		s = Square(side)
		s.area()

	@unittest.expectedFailure
	def test_string(self):
		side = "side"
		s = Square(side)
		s.area()
