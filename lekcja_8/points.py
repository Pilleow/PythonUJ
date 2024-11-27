import unittest


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 4)
        self.p3 = Point(1, 2)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(str(self.p2), "(3, 4)")

    def test_eq(self):
        self.assertEqual(self.p1, self.p3)
        self.assertNotEqual(self.p1, self.p2)

    def test_add(self):
        result = self.p1 + self.p2
        self.assertEqual(result, Point(4, 6))

    def test_sub(self):
        result = self.p1 - self.p2
        self.assertEqual(result, Point(-2, -2))

    def test_mul(self):
        result = self.p1 * self.p2
        self.assertEqual(result, 11)

    def test_cross(self):
        result = self.p1.cross(self.p2)
        self.assertEqual(result, -2)

    def test_length(self):
        self.assertAlmostEqual(self.p1.length(), (1 ** 2 + 2 ** 2) ** 0.5)
        self.assertAlmostEqual(self.p2.length(), (3 ** 2 + 4 ** 2) ** 0.5)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash(self.p3))
        self.assertNotEqual(hash(self.p1), hash(self.p2))


if __name__ == "__main__":
    unittest.main()
