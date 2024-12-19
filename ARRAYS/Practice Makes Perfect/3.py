# Tablica zawierająca liczby
numbers = [8, 2, 5, 1, 9]

# Obliczanie drugiej potęgi każdej liczby w tablicy
squared_numbers = [num ** 2 for num in numbers]

# Wypisanie oryginalnej tablicy
print("Array:", *numbers)

# Wypisanie drugich potęg liczb
print("2nd power:", *squared_numbers)
