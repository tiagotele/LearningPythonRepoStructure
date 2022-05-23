from shape.square import Square
from random import randrange
import pytest

class TestSquare():

	def test_single_square_area(self):
		side = 3.0
		expected_area = 9.0
		s = Square(side)
		assert s.area() == expected_area

	def test_random_side_area(self):
		side = randrange(100)
		expected_area = side*side
		s = Square(side)
		assert s.area() == expected_area
	

	def test_negative_side(self):
		with pytest.raises(Exception):
			side = -3
			s = Square(side)
			s.area()

	def test_string(self):
		with pytest.raises(Exception):
			side = "side"
			s = Square(side)
			s.area()
