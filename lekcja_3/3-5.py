'''
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć
liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod
znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
'''

from math import log10


def getMiarka(length: int) -> str:
    SEGMENTBREAK = "|"
    SEGMENT = "...."
    outstr = SEGMENTBREAK + (SEGMENT + SEGMENTBREAK) * length + "\n0"
    digitcount = int(log10(length)) + 1
    for i in range(1, length + 1):
        outstr += ' ' * (len(SEGMENT) + 1 - digitcount) + str(i).rjust(digitcount)
    return outstr


if __name__ == "__main__":
    length = int(input("Długość miarki: "))
    miarka = getMiarka(length)
    print(miarka)
