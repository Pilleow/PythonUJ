
def printExceptMultiplesOf3(min: int, max: int) -> None:
    for i in range(min, max + 1):
        if i % 3 != 0: print(i)

if __name__ == '__main__':
    printExceptMultiplesOf3(0, 30)
