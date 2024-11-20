import random


def iter_01():
    while True:
        yield from (0, 1)


def iter_rand_direction():
    while True:
        yield random.choice(("N", "E", "S", "W"))


def iter_weekday():
    while True:
        yield from range(7)


if __name__ == '__main__':
    print("Przemiennie 0, 1: ")
    a = iter_01()
    for _ in range(10):
        print(next(a), end=", ")

    print("\nLosowy kierunek: ")
    b = iter_rand_direction()
    for _ in range(10):
        print(next(b), end=", ")

    print("\nDni tygodnia: ")
    c = iter_weekday()
    for _ in range(15):
        print(next(c), end=", ")
