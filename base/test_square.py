from .square import Square
import unittest

class TestSquare(unittest.TestCase):

	def test_square_area(self):
		expected_area = 9
		side = 3
		s = Square(3)
		self.assertEqual(s.area(), expected_area)
