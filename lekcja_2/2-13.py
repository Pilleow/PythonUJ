# Igor Zamojski
# Zadanie 2.13


def cumulativeWordLength(line: str) -> int:
    return sum([len(w) for w in line.strip().split()])


if __name__ == "__main__":
    assert cumulativeWordLength("  ") == 0
    assert cumulativeWordLength("hello world") == 10
    assert cumulativeWordLength("this  is an  example string   ") == 21
