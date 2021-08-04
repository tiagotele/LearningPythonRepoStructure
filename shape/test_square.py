from shape.square import Square
import unittest

class TestSquare(unittest.TestCase):

	def test_square_area(self):
		expected_area = 9
		side = 3
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
