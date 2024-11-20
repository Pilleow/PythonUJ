import unittest

from math import pi
from circle import Circle
from points import Point


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(0, 0, 1)
        self.c2 = Circle(4, 0, 1)
        self.c3 = Circle(0, 0, 5)
        self.c4 = Circle(3, 0, 2)
        self.c5 = Circle(1, 1, 1)
        self.c6 = Circle(1, 1, 5)

    def test_equality(self):
        self.assertEqual(self.c1, Circle(0, 0, 1))
        self.assertNotEqual(self.c1, self.c2)

    def test_area(self):
        self.assertAlmostEqual(self.c1.area(), pi, places=5)
        self.assertAlmostEqual(self.c3.area(), 25 * pi, places=5)

    def test_move(self):
        self.c1.move(3, 4)
        self.assertEqual(self.c1.pt, Point(3, 4))
        self.c2.move(-1, -2)
        self.assertEqual(self.c2.pt, Point(3, -2))

    def test_cover_no_overlap(self):
        result = self.c1.cover(self.c2)
        self.assertAlmostEqual(result.pt.x, 2, places=5)
        self.assertAlmostEqual(result.pt.y, 0, places=5)
        self.assertAlmostEqual(result.radius, 3, places=5)

    def test_cover_partial_overlap(self):
        result = self.c3.cover(self.c6)
        self.assertAlmostEqual(result.pt.x, 0.5, places=5)
        self.assertAlmostEqual(result.pt.y, 0.5, places=5)
        self.assertAlmostEqual(result.radius, 5.707106, places=5)

    def test_cover_fully_contained(self):
        result = self.c3.cover(self.c5)
        self.assertEqual(result, self.c3)


if __name__ == "__main__":
    unittest.main()
