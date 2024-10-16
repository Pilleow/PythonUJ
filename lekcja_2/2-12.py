# Igor Zamojski
# Zadanie 2.12


def firstAndLastLetters(line: str) -> list[str]:
    lastLetters = ""
    firstLetters = ""
    for w in line.split(" "):
        if len(w) == 0:
            continue
        lastLetters += w[-1]
        firstLetters += w[0]
    return [firstLetters, lastLetters]


if __name__ == '__main__':
    assert firstAndLastLetters("this is an example string") == ["tiaes", "ssneg"]
    assert firstAndLastLetters("  hello   world  ") == ["hw", "od"]
