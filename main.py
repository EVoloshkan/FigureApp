from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

c = Circle(2)

triangle = Triangle(10, 2, 15)
print(triangle.name)
print(triangle.perimeter)
print(triangle.area)
print()

rectangle = Rectangle(10, 2)
print(rectangle.name)
print(rectangle.perimeter)
print(rectangle.area)
print(rectangle.add_area(triangle))
print()

square = Square(1)
print(square.name)
print(square.perimeter)
print(square.area)
print()

circle = Circle(10)
print(circle.name)
print(circle.perimeter)
print(circle.area)
print()
