from src.shape.shape import Shape


class Rectangle(Shape):
    width = 0.0
    length = 0.0

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        if self.width <= 0.0 or self.length <= 0.0:
            raise ValueError("That is not a positive number!")
        return round(self.width * self.length, 2)
