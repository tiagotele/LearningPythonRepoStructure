from .shape import Shape

class Rectangle(Shape):
	width = 0
	length = 0 

	def __init__(self, width, length):
		self.width = width
		self.length = length

	def area(self):
		return self.width * self.length
