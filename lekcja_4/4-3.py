'''
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
'''

import math


def factorial(n: int) -> int:
    out = n
    for i in range(1, n):
        out *= i
    return out


if __name__ == "__main__":
    for i in range(1, 11):
        assert factorial(i) == math.factorial(i)
