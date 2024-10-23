# Ten kod składniowo jest prawidłowy, jednak średniki są niepotrzebne.
x = 2;
y = 3;
if (x > y):
    result = x;
else:
    result = y;

# Ten kod nie zadziała, ponieważ if statement musi być w nowej linii.
# for i in "axby": if ord(i) < 100: print (i)
# Poniżej poprawiona wersja:
for i in "axby":
    if ord(i) < 100: print(i)

# Ten kod jest prawidłowy, jednak dobrą sugestią byłoby przesunięcie print(...) do nowej linii.
for i in "axby": print(ord(i) if ord(i) < 100 else i)
