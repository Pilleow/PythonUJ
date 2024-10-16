# Igor Zamojski
# Zadanie 2.11


def interlaceWordWithUnderscore(word: str) -> str:
    word = word.strip()
    return "".join([s + "_" if s != word[-1] else s for s in word]) if len(word) > 0 else ""


if __name__ == '__main__':
    assert interlaceWordWithUnderscore("") == ""
    assert interlaceWordWithUnderscore("a") == "a"
    assert interlaceWordWithUnderscore("abc") == "a_b_c"
    assert interlaceWordWithUnderscore("abcdef") == "a_b_c_d_e_f"
