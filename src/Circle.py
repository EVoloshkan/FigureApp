import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError(f"Incorrect value r = {r}")

        self._r = r

    @property
    def area(self):
        return math.pi * math.pow(self._r, 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self._r
