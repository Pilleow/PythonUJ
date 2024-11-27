from math import pi

import pytest

from circle import Circle
from points import Point


@pytest.fixture
def circles():
    return {
        "c1": Circle(0, 0, 1),
        "c2": Circle(4, 0, 1),
        "c3": Circle(0, 0, 5),
        "c4": Circle(3, 0, 2),
        "c5": Circle(1, 1, 1),
        "c6": Circle(1, 1, 5),
    }


def test_equality(circles):
    c1 = circles["c1"]
    c2 = circles["c2"]
    assert c1 == Circle(0, 0, 1)
    assert c1 != c2


def test_area(circles):
    c1 = circles["c1"]
    c3 = circles["c3"]
    assert pytest.approx(c1.area(), rel=1e-5) == pi
    assert pytest.approx(c3.area(), rel=1e-5) == 25 * pi


def test_move(circles):
    c1 = circles["c1"]
    c2 = circles["c2"]
    c1.move(3, 4)
    assert c1.pt == Point(3, 4)
    c2.move(-1, -2)
    assert c2.pt == Point(3, -2)


def test_cover_no_overlap(circles):
    c1 = circles["c1"]
    c2 = circles["c2"]
    result = c1.cover(c2)
    assert pytest.approx(result.pt.x, rel=1e-5) == 2
    assert pytest.approx(result.pt.y, rel=1e-5) == 0
    assert pytest.approx(result.radius, rel=1e-5) == 3


def test_cover_partial_overlap(circles):
    c3 = circles["c3"]
    c6 = circles["c6"]
    result = c3.cover(c6)
    assert pytest.approx(result.pt.x, rel=1e-5) == 0.5
    assert pytest.approx(result.pt.y, rel=1e-5) == 0.5
    assert pytest.approx(result.radius, rel=1e-5) == 5.707106


def test_cover_fully_contained(circles):
    c3 = circles["c3"]
    c5 = circles["c5"]
    result = c3.cover(c5)
    assert result == c3


def test_properties(circles):
    c1 = circles["c1"]
    assert c1.top == 1
    assert c1.bottom == -1
    assert c1.right == 1
    assert c1.left == -1
    assert c1.width == 2
    assert c1.height == 2
    assert c1.topright == Point(1, 1)
    assert c1.bottomright == Point(1, -1)
    assert c1.topleft == Point(-1, 1)
    assert c1.bottomleft == Point(-1, -1)

    c4 = circles["c4"]
    assert c4.top == 2
    assert c4.bottom == -2
    assert c4.right == 5
    assert c4.left == 1
    assert c4.width == 4
    assert c4.height == 4
    assert c4.topright == Point(5, 2)
    assert c4.bottomright == Point(5, -2)
    assert c4.topleft == Point(1, 2)
    assert c4.bottomleft == Point(1, -2)


def test_circle_from_points():
    c = Circle.from_points([Point(1, 3), Point(0, 0), Point(6, -1)])
    print(c)
    assert pytest.approx(c.pt.x, rel=1e-8) == 3.1842105263157894
    assert pytest.approx(c.pt.y, rel=1e-8) == 0.6052631578947368
    assert pytest.approx(c.radius, rel=1e-8) == 3.24122510267414

    c = Circle.from_points([Point(1.815287, 3.1525), Point(-0.5511, 2.14251), Point(5.687351, -3.51985532)])
    assert pytest.approx(c.pt.x, rel=1e-8) == 2.2197930397213046
    assert pytest.approx(c.pt.y, rel=1e-8) == -1.0724442576188693
    assert pytest.approx(c.radius, rel=1e-8) == 4.244264260876986
