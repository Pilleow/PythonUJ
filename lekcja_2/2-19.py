# Igor Zamojski
# Zadanie 2.19


def buildStringFromIntegers(l: list) -> str:
    return " ".join([str(n).zfill(3) for n in l])


if __name__ == '__main__':
    assert buildStringFromIntegers([]) == ""
    assert buildStringFromIntegers([99]) == "099"
    assert buildStringFromIntegers([0, 1, 2]) == "000 001 002"
    assert buildStringFromIntegers([1, 22, 333]) == "001 022 333"
    assert buildStringFromIntegers([111, 222, 333]) == "111 222 333"
