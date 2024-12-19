# Tworzymy dwuwymiarową tablicę o rozmiarze 2x4
array = [
    [1, 2, 3, 4],  # Wiersz 1
    [5, 6, 7, 8]   # Wiersz 2
]

# Przechodzimy przez każdy wiersz i drukujemy jego elementy
for row in array:
    for element in row:
        print(element, end=" ")  # "end=' '" sprawia, że elementy będą drukowane w tej samej linii
    print()  # Po każdym wierszu drukujemy nową linię
