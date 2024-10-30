'''
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
'''

import sympy


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    for i in range(1, 11):
        assert fibonacci(i) == sympy.fibonacci(i)
