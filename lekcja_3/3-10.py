'''
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
(z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka
sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący
całą liczbę [funkcja roman2int()].
'''

def roman2int(roman: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    '''
    można słownik stworzyć w ten sposób, ale można też użyć dwóch list:
        roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        arabic_values = [1, 5, 10, 50, 100, 500, 1000]
    '''

    result = sum(values[c] for c in roman)
    for i in range(len(roman) - 1):
        if values[roman[i]] < values[roman[i + 1]]:
            result -= 2 * values[roman[i]]
            # Korekta dla mniejszych wartości przed większymi, tzn. typu IX, IV itd.
    return result


if __name__ == '__main__':
    assert roman2int('MCMXCIV') == 1994
    assert roman2int('LVIII') == 58
    assert roman2int('IX') == 9
    assert roman2int('MMMCDXLVII') == 3447
