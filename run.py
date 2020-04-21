from base.square import Square
from base.rectangle import Rectangle

def main():
	print ("On main method")

if __name__ == "__main__":
	main()

s = Square(4)
print ("Square area is ", s.area())

r = Rectangle(3,4)
print ("Rectangle area is", r.area())
