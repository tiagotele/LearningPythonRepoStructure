from src.shape.shape import Shape
import math

class Circle(Shape):
	radius = 0.0

	def __init__(self, radius):
		self.radius = radius

	def area(self):
		if self.radius <= 0.0:
			raise ValueError("That is not a positive number!")
		return round(math.pi*(self.radius**2), 2)

