from .shape import Shape

class Square(Shape):
	side = 0

	def __init__(self, side):
		self.side = side	
	
	def area(self):
		if self.side <= 0:
			raise ValueError("That is not a positive number!")
		return round(self.side*self.side, 2)
