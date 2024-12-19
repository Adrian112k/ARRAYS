# Tworzenie dwuwymiarowej tablicy 3x5
arr = [
    [1, 2, 3, 4, 5],   # Pierwszy wiersz
    [6, 7, 8, 9, 10],  # Drugi wiersz
    [11, 12, 13, 14, 15] # Trzeci wiersz
]

# Funkcja do drukowania tablicy w formie wierszy i kolumn
def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))

# Drukowanie tablicy przed zmianą
print("Array before swap:")
print_array(arr)

# Zamiana pierwszej i ostatniej kolumny
for row in arr:
    row[0], row[4] = row[4], row[0]

# Drukowanie tablicy po zmianie
print("\nArray after swap:")
print_array(arr)