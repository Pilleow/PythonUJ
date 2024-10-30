'''
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone
podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez
isinstance(item, (list, tuple)).
'''


def sum_seq(sequence: list) -> int:
    total_sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total_sum += sum_seq(item)
        else:
            total_sum += item
    return total_sum


if __name__ == '__main__':
    assert sum_seq([]) == 0
    assert sum_seq([1, 2, 3]) == 6
    assert sum_seq([1, 2, [1, 2], 4, [1, 2, 2]]) == 15
