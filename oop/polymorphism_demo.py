# polymorphism_demo.py

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Using exponentiation (** 2) to calculate the area
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
