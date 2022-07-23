import pytest

from src.Square import Square


def test_name_positive():
    square = Square(7)
    assert square.name == 'Square'


def test_name_negative():
    square = Square(5)
    assert square.name != 'RRR'


def test_exist_positive():
    Square(4)
    pass


@pytest.mark.parametrize("cond", [0, -3])
def test_exist_negative(cond):
    with pytest.raises(ValueError):
        Square(cond)


def test_area_positive():
    square = Square(3)
    assert square.area > 0
    assert square.area == 9


def test_perimetr_positive():
    square = Square(7)
    assert square.perimeter > 0
    assert square.perimeter == 28
