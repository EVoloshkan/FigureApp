import math
import src.Figure


class Square(src.Figure.Figure):
    def __init__(self, a):
        if a <= 0:
            raise ValueError(f"Incorrect value a {a}")

        self._a = a

    @property
    def area(self):
        return math.pow(self._a, 2)

    @property
    def perimeter(self):
        return self._a * 4
