# Igor Zamojski
# Zadanie 2.10


def countWordsInLine(line: str) -> int:
    line = line.strip()
    return sum([line[i].isspace() and not line[i - 1].isspace() for i in range(1, len(line))]) + 1 if len(line) > 0 else 0


if __name__ == '__main__':
    assert countWordsInLine("") == 0
    assert countWordsInLine(" ") == 0
    assert countWordsInLine("hello") == 1
    assert countWordsInLine("hello world") == 2
    assert countWordsInLine("hello\nworld") == 2
    assert countWordsInLine("  hello       world     ") == 2
    assert countWordsInLine("this is an example string") == 5
    assert countWordsInLine(" język\tpython! ") == 2
