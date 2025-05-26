# Exercise 1
# Polymorphism
# Create a Python program that explores polymorphism using a hierarchy of shapes. Start
# with a base class Shape, and then create two or more derived classes (e.g., Circle,
# Rectangle, Triangle) that inherit from the Shape class. Each shape class should have its
# own implementation of methods like area() and perimeter(). These methods will
# calculate the area and perimeter of the respective shape.
# 1. Define the Shape base class with methods like area() and perimeter(). You can
# initialize any common attributes in the base class.
# 2. Create derived classes for diƯerent shapes, e.g., Circle, Rectangle, and
# Triangle. Each derived class should inherit from the Shape base class and
# implement its own version of the area() and perimeter() methods.
# 3. Implement specific methods for each derived class. For example, the Circle
# class might have a method to calculate its area based on the radius, and the
# Rectangle class could have a method to calculate its area based on length and
# width.
# Create instances of each shape type and demonstrate the use of polymorphism
# by calling the area() and perimeter() methods on them.

from math import pi
class Shape:
    def area(self):
        return "The base class shape has no area"
    def perimiter(self):
        return "The base class shape has no perimiter"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimiter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimiter(self):
        return 2 * (self.length + self.width)
class Triangle(Shape):
    def __init__(self, base ,height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimiter(self):
        return self.side1 + self.side2 + self.side3

shapes = [
    Circle(radius=5),
    Rectangle(length=4, width=6),
    Triangle(base=6, height=4, side1=3, side2=4, side3=5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: ")
    print(f"Area: {shape.area()}")
    print(f"Perimiter: {shape.perimiter()}")



# Exercise 2
# Implement a Plugin System Using Duck Typing
# Create classes UpperCaseFormatter, LowerCaseFormatter, and TitleCaseFormatter
# that implement a format_text(text) method.
# Write a function apply_formatters(text, formatters) that applies a list of formatters to a
# string.
# Bonus:
# Add error handling to check if objects passed to apply_formatters actually have a
# format_text() method, raising a custom FormatterError if not.

import formatter

upper = formatter.UpperCaseFormatter()
lower = formatter.LowerCaseFormatter()
title = formatter.TitleCaseFormatter()

text = "This is my little TEXT. but. a little. longer."
formatters = [upper,lower,title]
result = formatter.apply_formatters(text, formatters)
print(f"Result {result}")

print(f"Upper: {upper.format_text(text)}")
print(f"Lower: {lower.format_text(text)}")
print(f"Title: {title.format_text(text)}")


