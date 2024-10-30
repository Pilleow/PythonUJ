'''
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n): pass
def make_grid(rows, cols): pass
'''

from math import log10


def make_ruler(n: int) -> str:
    SEGMENTBREAK = "|"
    SEGMENT = "...."
    outstr = SEGMENTBREAK + (SEGMENT + SEGMENTBREAK) * n + "\n0"
    digitcount = int(log10(n)) + 1
    for i in range(1, n + 1):
        outstr += ' ' * (len(SEGMENT) + 1 - digitcount) + str(i).rjust(digitcount)
    return outstr


def make_grid(rows: int, cols: int) -> str:
    CORNER = "+"
    VERTICAL = "|"
    HORIZONTAL = "---"
    rowstr = CORNER + (HORIZONTAL + CORNER) * cols + "\n" + VERTICAL + (' ' * len(HORIZONTAL) + VERTICAL) * cols
    outstr = (rowstr + "\n") * rows + CORNER + (HORIZONTAL + CORNER) * cols
    return outstr


if __name__ == '__main__':
    print(make_ruler(12) + '\n\n' + make_grid(4, 4))
