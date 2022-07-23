import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("cond, exp", [
    ((Circle(2), Circle(5)), 91.106186954104),
    ((Triangle(3, 2, 4), Triangle(5, 3, 5)), 10.059281520282655),
    ((Square(3), Square(6)), 45),
    ((Rectangle(5, 2), Rectangle(7, 3)), 31),
    ((Circle(3), Rectangle(2, 3)), 34.27433388230814),
    ((Rectangle(1, 4), Square(5)), 29),
    ((Square(2), Triangle(2, 2, 3)), 5.984313483298443),
    ((Triangle(3, 3, 3), Circle(4)), 54.162596774466664)
])
def test_add_area_positive(cond, exp):
    assert cond[0].add_area(cond[1]) == exp


@pytest.mark.parametrize("cond", [
    (Circle(2), 5),
    (Circle(3), 'slovo')
])
def test_add_area_negative(cond):
    with pytest.raises(ValueError):
        cond[0].add_area(cond[1])


@pytest.mark.parametrize("cond", [
    (Circle(2)),
    (Rectangle(3, 2)),
    (Square(3)),
    (Triangle(3, 5, 3))
])
def test_add_area_negative1(cond):
    with pytest.raises(ValueError):
        cond.add_area(Circle(-1))
