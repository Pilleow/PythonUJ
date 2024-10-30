'''
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
'''


def odwracanieIter(arr: list, left: int, right: int) -> list:
    middle = left + (right - left) // 2
    for i in range(0, right - left):
        arr[middle - i], arr[middle + i] = arr[middle + i], arr[middle - i]
    return arr


def odwracanieRec(arr: list, left: int, right: int) -> list:
    arr[left], arr[right] = arr[right], arr[left]
    if right - left > 1:
        arr = odwracanieRec(arr, left + 1, right - 1)
    return arr


if __name__ == '__main__':
    assert odwracanieIter([1, 2, 3, 4, 5], 2, 4) == [1, 2, 5, 4, 3]
    assert odwracanieRec([1, 2, 3, 4, 5], 2, 4) == [1, 2, 5, 4, 3]
