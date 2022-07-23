import pytest

from src.Rectangle import Rectangle


def test_name_positive():
    rectangle = Rectangle(7, 3)
    assert rectangle.name == 'Rectangle'


def test_name_negative():
    rectangle = Rectangle(5, 2)
    assert rectangle.name != 'RRR'


def test_exist_positive():
    Rectangle(4, 4)
    pass


@pytest.mark.parametrize("cond", [
    (0, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (-1, 1),
    (1, -1),
    (-1, -1)
])
def test_exist_negative(cond):
    with pytest.raises(ValueError):
        Rectangle(cond[0], cond[1])


def test_area_positive():
    rectangle = Rectangle(3, 7)
    assert rectangle.area > 0
    assert rectangle.area == 21


def test_perimetr_positive():
    rectangle = Rectangle(2, 5)
    assert rectangle.perimeter > 0
    assert rectangle.perimeter == 14
