# Igor Zamojski
# Zadanie 2.17


def sortAlphabetically(line: str) -> str:
    return " ".join(sorted(line.strip().split()))


def sortLengthily(line: str) -> str:
    return " ".join(sorted(line.strip().split(), key=len))


if __name__ == "__main__":
    assert sortAlphabetically("this is a string") == "a is string this"
    assert sortLengthily("this is a string") == "a is this string"
