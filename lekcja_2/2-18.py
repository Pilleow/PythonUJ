# Igor Zamojski
# Zadanie 2.18


def countZeros(n: int) -> int:
    return sum([d == "0" for d in str(n)])


if __name__ == '__main__':
    assert countZeros(0) == 1
    assert countZeros(1) == 0
    assert countZeros(152852985792) == 0
    assert countZeros(10528052980579020) == 5
    assert countZeros(10528052980579020006363620) == 8
