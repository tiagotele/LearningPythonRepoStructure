from .circle import Circle
import math
import unittest

class TestCircle(unittest.TestCase):

	def test_circle_area(self):
		radius = 9
		c = Circle(radius)
		self.assertEqual(c.area(), math.pi*(c.radius**2))
