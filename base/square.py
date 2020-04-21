from .shape import Shape

class Square(Shape):
	side = 0

	def __init__(self, side):
		self.side = side	
	
	def area(self):
		return self.side*self.side
