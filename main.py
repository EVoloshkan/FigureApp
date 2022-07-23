from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


figure = Figure()
print(figure.area)

triangle = Triangle(3, 2, 4)
print(triangle.name)
print(triangle.perimeter)
print(triangle.area)
print()

rectangle = Rectangle(2, 5)
print(rectangle.name)
print(rectangle.perimeter)
print(rectangle.area)
print(rectangle.add_area(triangle))
print()

square = Square(7)
print(square.name)
print(square.perimeter)
print(square.area)
print()

circle = Circle(10)
print(circle.name)
print(circle.perimeter)
print(circle.area)
print()
