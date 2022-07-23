import pytest

from src.Circle import Circle


def test_name_positive():
    circle = Circle(3)
    assert circle.name == 'Circle'


def test_name_negative():
    circle = Circle(5)
    assert circle.name != 'RRR'


def test_exist_positive():
    Circle(2)
    pass


@pytest.mark.parametrize("cond", [0, -1])
def test_exist_negative(cond):
    with pytest.raises(ValueError):
        Circle(cond)


def test_area_positive():
    circle = Circle(4)
    assert circle.area > 0
    assert circle.area == 50.26548245743669


def test_perimetr_positive():
    circle = Circle(8)
    assert circle.perimeter > 0
    assert circle.perimeter == 50.26548245743669



