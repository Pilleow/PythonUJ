
## Opis Projektu
Projekt umożliwia wizualizację drzew AVL i Binary Search Tree (BST). Narzędzie pozwala na wstawianie, usuwanie oraz wyszukiwanie węzłów w obu strukturach z animowanymi wizualizacjami, oferując interaktywny sposób zrozumienia algorytmów związanych z drzewami.

## Opis Plików
Poniżej znajduje się krótki opis każdego pliku w projekcie:

### 1. `avltree.py`
- Zawiera klasę `AVLTree`, która rozszerza klasę `BSTTree` o operacje specyficzne dla drzew AVL, takie jak rotacje (lewa i prawa) zapewniające zbalansowanie drzewa.
- Implementuje metody wstawiania i usuwania węzłów z zachowaniem równowagi drzewa AVL.
- Zawiera funkcje pomocnicze, takie jak obliczanie współczynnika równowagi i wysokości węzłów.

### 2. `bsttree.py`
- Implementuje klasę `BSTTree` do operacji na drzewach binarnych (BST).
- Umożliwia wstawianie, usuwanie, wyszukiwanie oraz przechodzenie drzewa (przedrostkowe, środkowe, przyrostkowe).
- Zawiera metody pomocnicze do znajdowania minimum, maksimum, następcy i poprzednika węzła.

### 3. `main.py`
- Główny skrypt inicjujący graficzny interfejs użytkownika (GUI) z wykorzystaniem biblioteki `pygame`.
- Zawiera klasę `App`, która obsługuje:
  - Renderowanie GUI
  - Interakcje użytkownika, takie jak wstawianie, usuwanie i wyszukiwanie węzłów
  - Przełączanie między wizualizacjami AVL i BST
  - Inicjalizację drzew i animacje
- Umożliwia pełną interakcję za pomocą klawiatury i myszy.

### 4. `node.py`
- Definiuje klasę `Node`, która reprezentuje pojedynczy węzeł drzewa.
- Każdy węzeł posiada atrybuty takie jak wartość, lewe i prawe dziecko, rodzic oraz głębokość.

### Uwaga: Rysowanie drzewa

Rysowanie drzewa jest realizowane w funkcji `render_tree()` w pliku `main.py`, która działa w pętli głównej aplikacji. Kluczowe kroki to:

1. Obliczenie odstępów i pozycji węzłów
  - Dla każdego poziomu drzewa (`depth`) obliczana jest liczba węzłów, które muszą być narysowane (`count_nodes_per_depth()`).
  - Wartości te są używane do określenia szerokości (`x_node_span`), która definiuje maksymalny zakres pozycji węzłów na danym poziomie.
2. Rekursyjne rysowanie węzłów
  - Funkcja `calculate_point_recursive()` jest odpowiedzialna za rysowanie drzewa w sposób rekurencyjny:
    - Funkcja przyjmuje aktualny węzeł, pozycję rodzica, zakresy pozycji (`min_x`, `max_x`), głębokość węzła (`y`) oraz rodzica węzła.
    - Dla każdego węzła funkcja rekurencyjnie przechodzi do jego lewego i prawego potomka, obliczając ich pozycje w układzie współrzędnych.
3. Rysowanie węzłów i krawędzi
  - Jeśli węzeł ma rodzica, rysowane są linie łączące go z rodzicem. Kolor linii zależy od tego, czy węzeł jest lewym, czy prawym dzieckiem.
  - Węzły są rysowane jako okręgi z wartością w środku. Okręgi mają różne kolory w zależności od tego, czy węzeł jest aktywny, wyróżniony, czy pasywny (np. w trakcie animacji wyszukiwania).
  - W przypadku trybu AVL przy każdym węźle wyświetlany jest jego czynnik równowagi (balance_factor), który jest obliczany przez `calc_balance_factor()`.

## Instalacja i Uruchomienie

### Wymagania
Przed rozpoczęciem upewnij się, że masz zainstalowane:
- Python 3.8 lub nowszy
- Bibliotekę `pygame`

Instalacja `pygame`:
```bash
pip install pygame
```

### Jak Uruchomić Program
1. Pobierz lub sklonuj pliki projektu.
2. Umieść wszystkie pliki w jednym katalogu.
3. Uruchom program poleceniem:
   ```bash
   python main.py
   ```

### Sterowanie i Funkcje
- **Tryby Wizualizacji Drzew**:
  - Naciśnij `C`, aby przełączać się między widokami AVL i BST.
- **Operacje na Węzłach**:
  - `I`: Włącz tryb wstawiania i wpisz wartość do wstawienia.
  - `D`: Włącz tryb usuwania i wpisz wartość do usunięcia.
  - `S`: Włącz tryb wyszukiwania i wpisz wartość do wyszukania.
  - Po wybraniu operacji oraz wpisaniu wartości, wciśnij **Enter** aby przeprowadzić wybraną operację.
- **Powiększanie i Pomniejszanie**:
  - `+` lub `-`: Powiększ lub pomniejsz widok.
- **Zmiana Rozmiaru Drzewa**:
  - `↑` lub `↓`: Zwiększ lub zmniejsz liczbę węzłów (operacja generuje nowe drzewo).
- **Szybkość Animacji**:
  - `←` lub `→`: Zmień szybkość animacji.
 
## Autor
Igor Zamojski, w ramach kursu *Język Python 2024/2025* na piątym semestrze studiów *Informatyka Stosowana* na *Uniwersytecie Jagiellońskim*.

## Źródła
- [geeksforgeeks.org](https://www.geeksforgeeks.org/)
- [w3schools.com](https://www.w3schools.com/dsa)
- [wikipedia.org (AVL Tree)](https://en.wikipedia.org/wiki/AVL_tree)
- [wikipedia.org (BST Tree)](https://en.wikipedia.org/wiki/Binary_search_tree)
