from .shape import Shape
import math

class Circle(Shape):
	radius = 0

	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi*(self.radius**2)

