Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... class GeometricFigure:
...     def area(self):
...         pass
... 
... class Rectangle(GeometricFigure):
...     def __init__(self, width, height):
...         self.width = width
...         self.height = height
... 
...     def area(self):
...         return self.width * self.height
... 
... class Circle(GeometricFigure):
...     def __init__(self, radius):
...         self.radius = radius
... 
...     def area(self):
...         return math.pi * self.radius ** 2
... 
... class Rhomb(GeometricFigure):
...     def __init__(self, diagonal1, diagonal2):
...         self.diagonal1 = diagonal1
...         self.diagonal2 = diagonal2
... 
...     def area(self):
...         return (self.diagonal1 * self.diagonal2) / 2
... 
... rectangle = Rectangle(8, 12)
... circle = Circle(7)
... rhombus = Rhomb(14, 18)
... 
... print("Площадь прямоугольника:", rectangle.area())
... print("Площадь круга:", circle.area())
... print("Площадь ромба:", rhombus.area())
