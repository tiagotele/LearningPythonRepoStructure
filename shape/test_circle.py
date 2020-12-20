from .circle import Circle
import math
from random import randrange
import unittest

class TestCircle(unittest.TestCase):

	def test_single_circle_area(self):
		radius = 9
		c = Circle(radius)
		self.assertEqual(c.area(), round( math.pi*(c.radius**2), 2) )
		
	def test_random_circle_area(self):
		radius = randrange(100)
		c = Circle(radius)
		self.assertEqual(c.area(), round( math.pi*(c.radius**2), 2) )

	@unittest.expectedFailure
	def test_negative_radius_circle_area(self):
		radius = -randrange(100)
		c = Circle(radius)
		self.assertEqual(c.area(), round( math.pi*(c.radius**2), 2) )

