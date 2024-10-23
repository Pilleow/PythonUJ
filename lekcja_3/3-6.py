'''
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
'''

def getProstokat(y: int, x: int) -> str:
    CORNER = "+"
    VERTICAL = "|"
    HORIZONTAL = "---"
    outstr = ""

    rowstr = CORNER + (HORIZONTAL + CORNER) * x + "\n" + VERTICAL + (' ' * len(HORIZONTAL) + VERTICAL) * x
    outstr = (rowstr + "\n") * y + CORNER + (HORIZONTAL + CORNER) * x

    return outstr


if __name__ == '__main__':
    x, y = list(map(int, input("I (np. 2x4):").rstrip().split("x")))
    prostokat = getProstokat(x, y)
    print(prostokat)
