from shape.square import Square
from shape.rectangle import Rectangle
from shape.circle import Circle

def main():
	print ("On main method")

if __name__ == "__main__":
	main()

s = Square(4)
print ("Square area is ", s.area())

r = Rectangle(3,4)
print ("Rectangle area is", r.area())

c = Circle(4)
print ("Circle area is ", c.area())
