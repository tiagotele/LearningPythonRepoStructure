from shape.circle import Circle
import math
from random import randrange
import pytest


class TestCircle:
    def test_single_circle_area(self):
        radius = 9
        c = Circle(radius)
        assert c.area() == round(math.pi * (c.radius**2), 2)

    def test_random_circle_area(self):
        radius = randrange(100)
        c = Circle(radius)
        assert c.area() == round(math.pi * (c.radius**2), 2)

    def test_negative_radius_circle_area(self):
        with pytest.raises(Exception):
            radius = -randrange(100)
            c = Circle(radius)
            c.area()
