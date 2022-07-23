import math
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a > b + c or b > a + c or c > a + b:
            raise ValueError(f"Triangle with given sides {a}, {b}, {c} does not exist")

        self._a = a
        self._b = b
        self._c = c

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    @property
    def perimeter(self):
        return self._a + self._b + self._c
