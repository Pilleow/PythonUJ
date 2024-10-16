# Igor Zamojski
# Zadanie 2.12


def firstAndLastLetters(line: str) -> list[str]:
    return [
        "".join([s[0] for s in line.strip().split()]),
        "".join([s[-1] for s in line.strip().split()])
    ]


if __name__ == '__main__':
    assert firstAndLastLetters("this is an example string") == ["tiaes", "ssneg"]
    assert firstAndLastLetters("  hello   world  ") == ["hw", "od"]
