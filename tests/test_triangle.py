import pytest

from src.Triangle import Triangle


def test_name_positive():
    triangle = Triangle(4, 3, 2)
    assert triangle.name == 'Triangle'


def test_name_negative():
    triangle = Triangle(5, 2, 6)
    assert triangle.name != 'RRR'


def test_exist_positive():
    Triangle(4, 4, 4)
    pass


@pytest.mark.parametrize("cond", [
    (0, 0, 0),
    (-1, -1, -1),
    (5, 1, 3),
    (2, 7, 4),
    (3, 6, 10),
    (3, 2, 5)
])
def test_exist_negative(cond):
    with pytest.raises(ValueError):
        Triangle(cond[0], cond[1], cond[2])


def test_area_positive():
    triangle = Triangle(3, 2, 4)
    assert triangle.area > 0
    assert triangle.area == 2.9047375096555625


def test_perimetr_positive():
    triangle = Triangle(2, 5, 5)
    assert triangle.perimeter > 0
    assert triangle.perimeter == 12
