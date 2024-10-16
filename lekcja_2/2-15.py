# Igor Zamojski
# Zadanie 2.15


def stringFromLDigits(l: list) -> str:
    return ''.join([str(d) for d in l]) if len(l) > 0 else ""


if __name__ == '__main__':
    assert stringFromLDigits([]) == ""
    assert stringFromLDigits([0]) == "0"
    assert stringFromLDigits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == "123456789"
    assert stringFromLDigits([142, 56]) == "14256"
