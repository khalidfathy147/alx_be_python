import math

class Shape:
    """Represents a general shape."""

    def area(self):
        """Raises NotImplementedError, as area calculation is specific to subclasses."""
        raise NotImplementedError("Area method must be implemented by subclasses.")

class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, length, width):
        """Initializes a Rectangle object."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initializes a Circle object."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius**2