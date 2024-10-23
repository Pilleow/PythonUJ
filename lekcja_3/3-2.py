
L = [3, 5, 4]
L = L.sort()
# Tu jest OK

# x, y = 1, 2, 3
# Tutaj przydzielamy więcej wartości niż mamy zmiennych - musimy usunąć jedną wartość
x, y = 1, 2

X = 1, 2, 3
# X[1] = 4
# Tutaj nie możemy zmienić wartości X[1] ponieważ X=1,2,3 interpretowane jest jako tuple, a tuple w pythonie są stałe.

X = [1, 2, 3]
# X[3] = 4
# Tu maksymalny indeks X to 2, więc jeśli chcemy na trzecim miejscu wstawić 4 to musimy zrobić X.append(4)
X.append(4)

X = "abc"
# X.append("d")
# String nie posiada metody .append(...). Aby dodać coś pod koniec tekstu musimy zrobić przykładowo konkatenację.
X += "d"

# L = list(map(pow, range(8)))
# Tutaj metoda pow wymaga dwóch argumentów, ale my tylko dajemy jeden. Należy dodać argument exponent, przykładowo 2.
L = list(map(lambda x: pow(x, 2), range(8)))
