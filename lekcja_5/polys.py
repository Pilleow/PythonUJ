'''
Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach.
Wielomian będzie reprezentowany przez listę swoich współczynników,
np. [a0, a1, a2] dla a0 + a1*x + a2*x*x. Napisać kod testujący moduł polys.
'''

from typing import List


def _pad_arr_to_length(arr: List[int], target_len: int) -> List[int]:
    return arr + [0] * (target_len - len(arr))


def add_poly(poly1: List[int], poly2: List[int]) -> List[int]:
    max_len = max(len(poly1), len(poly2))
    poly1 = _pad_arr_to_length(poly1, max_len)
    poly2 = _pad_arr_to_length(poly2, max_len)
    return [a + b for a, b in zip(poly1, poly2)]


def sub_poly(poly1: List[int], poly2: List[int]) -> List[int]:
    max_len = max(len(poly1), len(poly2))
    poly1 = _pad_arr_to_length(poly1, max_len)
    poly2 = _pad_arr_to_length(poly2, max_len)
    return [a - b for a, b in zip(poly1, poly2)]


def mul_poly(poly1: List[int], poly2: List[int]) -> List[int]:
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coef1 in enumerate(poly1):
        for j, coef2 in enumerate(poly2):
            result[i + j] += coef1 * coef2
    return result


def is_zero(poly: List[int]) -> bool:
    for c in poly:
        if c != 0:
            return False
    return True


def eq_poly(poly1: List[int], poly2: List[int]) -> bool:
    while len(poly1) > 1 and poly1[-1] == 0:
        poly1.pop()
    while len(poly2) > 1 and poly2[-1] == 0:
        poly2.pop()
    return poly1 == poly2


def eval_poly(poly: List[int], x0: int) -> int:
    result = 0
    for coef in reversed(poly):
        result = result * x0 + coef
    return result


def combine_poly(poly1, poly2):
    result = [0]
    temp_poly = [1]
    for coef in poly1:
        term = [c * coef for c in temp_poly]
        result = add_poly(result, term)
        temp_poly = mul_poly(temp_poly, poly2)
    return result

def pow_poly(poly: List[int], n: int) -> List[int]:
    if n == 0:
        return [1]
    if n == 1:
        return poly
    result = poly
    for _ in range(1, n):
        result = mul_poly(result, poly)
    return result


def diff_poly(poly):
    return [(i * coef) for i, coef in enumerate(poly)][1:]
