# Igor Zamojski
# Zadanie 2.14


def longestWord(line: str) -> list:
    line = line.strip()
    longestWord = sorted(line.split(), key=len)[-1] if len(line) > 0 else ""
    return [longestWord, len(longestWord)]


if __name__ == '__main__':
    assert longestWord("") == ['', 0]
    assert longestWord("      ") == ['', 0]
    assert longestWord("Hello world!") == ['world!', 6]
    assert longestWord("  this  is an  example string  ") == ['example', 7]
