'''
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji.

Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
'''


def sum2Dinto1D(arr2d: list) -> list[int]:
    for i in range(len(arr2d)):
        arr2d[i] = sum(arr2d[i])
    return arr2d


if __name__ == '__main__':
    assert sum2Dinto1D([[], [4], (1, 2), [3, 4], (5, 6, 7)]) == [0, 4, 3, 7, 18]
