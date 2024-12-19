# Tworzymy dwuwymiarową tablicę
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Inicjalizujemy zmienną do sumowania
sum_last_column = 0

# Przechodzimy przez każdy wiersz i dodajemy ostatnią kolumnę do sumy
for row in array:
    sum_last_column += row[-1]  # row[-1] to ostatni element w wierszu

# Drukujemy wynik
print("Suma wartości w ostatniej kolumnie:", sum_last_column)
