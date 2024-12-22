
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
