'''

Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się
nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich
elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez
isinstance(item, (list, tuple)).
'''


def flatten(sequence: list) -> list[int]:
    i = 0
    while i < len(sequence):
        if isinstance(sequence[i], (list, tuple)):
            sequence[i:i + 1] = flatten(sequence[i])
        i += 1
    return sequence


if __name__ == '__main__':
    assert flatten([]) == []
    assert flatten([1, 2, [1, 2], 4, [1, 2, 2]]) == [1, 2, 1, 2, 4, 1, 2, 2]
