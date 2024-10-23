'''
Dla dwóch sekwencji liczb lub znaków znaleźć:
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
'''


# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
def getCharIntersection(a_seq: str, b_seq: str) -> list[str]:
    return list(set(b_seq).intersection(a_seq))


# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
def getCharUnion(a_seq: str, b_seq: str) -> list[str]:
    return list(set(b_seq).union(a_seq))


if __name__ == '__main__':
    assert sorted(getCharIntersection("123456789", " 2 4 6 89")) == ['2', '4', '6', '8', '9']
    assert sorted(getCharIntersection("mpty", "none")) == []
    assert sorted(getCharIntersection("1234", "1234")) == ['1', '2', '3', '4']
    assert sorted(getCharIntersection(" pace", "this ")) == [' ']

    assert sorted(getCharUnion("123456789", " 2 4 6 89")) == [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert sorted(getCharUnion("mpty", "none")) == ['e', 'm', 'n', 'o', 'p', 't', 'y']
