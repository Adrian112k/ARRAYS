# Funkcja tworząca dwuwymiarową tablicę wypełnioną zerami
def create_2d_arr(x, y):
    # Tworzymy dwuwymiarową tablicę o wymiarach x (wiersze) i y (kolumny)
    return [[0 for _ in range(y)] for _ in range(x)]

# Tworzymy dwuwymiarową tablicę 3x5
array = create_2d_arr(3, 5)

# Drukujemy tablicę
for row in array:
    print(row)
