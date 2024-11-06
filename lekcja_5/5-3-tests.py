import unittest

from polys import *


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [2, 1]  # W(x) = 2 + x
        self.p2 = [2, 1, 0]  # W(x) = 2 + x
        self.p3 = [-3, 0, 1]  # W(x) = -3 + x^2
        self.p4 = [3]  # W(x) = 3, wielomian zerowego stopnia
        self.p5 = [0]  # W(x) = 0
        self.p6 = [0, 0, 0]  # W(x) = 0
        self.p7 = [1, 0, -4, 0, 3, 2]  # W(x) = 1 - 4x^2 + 3x^4 + 2x^5
        self.p8 = [5, -3, 0, 7, 0, -6, 1, 0]  # W(x) = 5 - 3x + 7x^3 - 6x^5 + x^6

    def test_add_poly(self):
        self.assertTrue(eq_poly(add_poly(self.p1, self.p2), [4, 2, 0]))  # 2 + x + (2 + x) = 4 + 2x
        self.assertTrue(eq_poly(add_poly(self.p1, self.p3), [-1, 1, 1]))  # (2 + x) + (-3 + x^2) = -1 + x + x^2
        self.assertTrue(is_zero(add_poly(self.p5, self.p6)))  # 0 + 0 = 0
        self.assertTrue(eq_poly(add_poly(self.p7, self.p8), [6, -3, -4, 7, 3, -4, 1, 0]))

    def test_sub_poly(self):
        self.assertTrue(is_zero(sub_poly(self.p1, self.p2)))  # (2 + x) - (2 + x) = 0
        self.assertTrue(eq_poly(sub_poly(self.p3, self.p4), [-6, 0, 1]))  # (-3 + x^2) - 3 = -6 + x^2
        self.assertTrue(is_zero(sub_poly(self.p5, self.p6)))  # 0 - 0 = 0
        self.assertTrue(eq_poly(sub_poly(self.p7, self.p8), [-4, 3, -4, -7, 3, 8, -1, 0]))

    def test_mul_poly(self):
        self.assertTrue(eq_poly(mul_poly(self.p1, self.p3), [-6, -3, 2, 1]))  # (2 + x)(-3 + x^2) = -6 - 3x + 2x^2 + x^3
        self.assertTrue(eq_poly(mul_poly(self.p4, self.p4), [9]))  # 3 * 3 = 9
        self.assertTrue(is_zero(mul_poly(self.p5, self.p3)))  # 0 * (-3 + x^2) = 0
        self.assertTrue(eq_poly(mul_poly(self.p7, self.p8), [5, -3, -20, 19, 15, -33, -5, 45, 10, -18, -9, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.p5))
        self.assertTrue(is_zero(self.p6))
        self.assertFalse(is_zero(self.p1))
        self.assertFalse(is_zero(self.p7))
        self.assertFalse(is_zero(self.p8))

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p1, self.p2))  # W(x) = 2 + x == W(x) = 2 + x
        self.assertFalse(eq_poly(self.p1, self.p3))  # W(x) = 2 + x != W(x) = -3 + x^2
        self.assertTrue(eq_poly(self.p5, self.p6))  # W(x) = 0 == W(x) = 0
        self.assertFalse(eq_poly(self.p7, self.p8))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 1), 3)  # 2 + 1 = 3
        self.assertEqual(eval_poly(self.p3, 2), 1)  # -3 + 4 = 1
        self.assertEqual(eval_poly(self.p4, 10), 3)  # 3 w każdym punkcie
        self.assertEqual(eval_poly(self.p7, 2), 97)
        self.assertEqual(eval_poly(self.p8, -1), 8)

    def test_combine_poly(self):
        self.assertTrue(eq_poly(combine_poly(self.p1, self.p1), [4, 1]))  # (2 + (2 + x)) = 4 + x
        self.assertTrue(
            eq_poly(combine_poly(self.p3, self.p3), [6, 0, -6, 0, 1]))  # (-3 + (-3 + x^2)^2) = 6 - 6x^2 + x^4
        self.assertTrue(eq_poly(combine_poly(self.p3, self.p4), [6]))  # (-3 + (3)^2) = 6
        self.assertTrue(eq_poly(combine_poly(self.p7, self.p8), [
            8026, -23130, 26514, 38850, -119439, 59094, 218052, -349686, -57762, 619640,
            -422250, -563544, 929423, 40254, -1022430, 539902, 658932, -762432, -143664,
            575976, -130884, -272888, 142368, 65328, -58727, -462, 11280, -4250, 720,
            -60, 2
        ]))

    def test_pow_poly(self):
        self.assertTrue(eq_poly(pow_poly(self.p1, 2), [4, 4, 1]))  # (2 + x)^2 = 4 + 4x + x^2
        self.assertTrue(
            eq_poly(pow_poly(self.p3, 3), [-27, 0, 27, 0, -9, 0, 1]))  # (-3 + x^2)^3 = -27 + 27x^2 - 9x^4 + x^6
        self.assertTrue(eq_poly(pow_poly(self.p4, 4), [81]))  # (3)^4 = 81
        self.assertTrue(eq_poly(pow_poly(self.p7, 2), [1, 0, -8, 0, 22, 4, -24, -16, 9, 12, 4]))

    def test_diff_poly(self):
        self.assertTrue(eq_poly(diff_poly(self.p1), [1]))  # (2 + x)' = 1
        self.assertTrue(eq_poly(diff_poly(self.p3), [0, 2]))  # (-3 + x^2)' = 2x
        self.assertTrue(is_zero(diff_poly(self.p4)))  # 3' = 0
        self.assertTrue(eq_poly(diff_poly(self.p7), [0, -8, 0, 12, 10]))
        self.assertTrue(eq_poly(diff_poly(self.p8), [-3, 0, 21, 0, -30, 6]))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
