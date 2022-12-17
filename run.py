from src.shape.square import Square
from src.shape.rectangle import Rectangle
from src.shape.circle import Circle


def main():
    print("On main method")


if __name__ == "__main__":
    main()

s = Square(4.0)
print("Square area is ", s.area())

r = Rectangle(3.0, 4.0)
print("Rectangle area is", r.area())

c = Circle(4.0)
print("Circle area is ", c.area())
