import unittest

from points import Point


class Rectangle:
    def __init__(self, left, top, right, bottom):
        if right < left or top < bottom:
            raise ValueError(f"Invalid rectangle dimensions: {str(self)}")
        self.p_tl = Point(left, top)
        self.p_br = Point(right, bottom)

    def __str__(self):
        return f"[({self.p_tl.x}, {self.p_tl.y}), ({self.p_br.x}, {self.p_br.y})]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.p_tl == other.p_tl and self.p_br == other.p_br

    def __ne__(self, other):
        return not self.__eq__(other)

    def center(self):
        return Point(
            self.p_tl.x + (self.p_br.x - self.p_tl.x) / 2,
            self.p_br.y + (self.p_tl.y - self.p_br.y) / 2
        )

    def area(self):
        return abs((self.p_br.x - self.p_tl.x) * (self.p_br.y - self.p_tl.y))

    def move(self, x, y):
        self.p_tl.x += x
        self.p_tl.y += y
        self.p_br.x += x
        self.p_br.y += y


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1, 4, 4, 1)
        self.rect2 = Rectangle(0, 5, 5, 0)
        self.rect3 = Rectangle(1, 4, 4, 1)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(1, 4), (4, 1)]")
        self.assertEqual(str(self.rect2), "[(0, 5), (5, 0)]")

    def test_eq(self):
        self.assertEqual(self.rect1, self.rect3)
        self.assertNotEqual(self.rect1, self.rect2)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2.5, 2.5))
        self.assertEqual(self.rect2.center(), Point(2.5, 2.5))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 9)
        self.assertEqual(self.rect2.area(), 25)

    def test_move(self):
        self.rect1.move(1, 1)
        self.assertEqual(self.rect1.p_tl, Point(2, 5))
        self.assertEqual(self.rect1.p_br, Point(5, 2))

        self.rect2.move(-1, -1)
        self.assertEqual(self.rect2.p_tl, Point(-1, 4))
        self.assertEqual(self.rect2.p_br, Point(4, -1))


if __name__ == "__main__":
    unittest.main()
