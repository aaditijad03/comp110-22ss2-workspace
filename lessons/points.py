"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with it's x, y components."""
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * Float."""
        return Point(self.x * factor, self.y * factor)

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python."""
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, rhs: Point) -> Point:
        print("add was called.")
        return Point(self. x + rhs.x, self.y + rhs.y)
    
    def __getitem__(self, index: int) -> float:
        """Overload subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else: 
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])