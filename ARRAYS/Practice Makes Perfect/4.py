# Tablica zawierająca liczby
numbers = [-15, 8, -31, 47, -2, 19]

# Inicjalizacja zmiennych dla maksimum i minimum
max_num = numbers[0]
min_num = numbers[0]

# Pętla przechodząca przez tablicę
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Wypisanie maksymalnej i minimalnej liczby
print("Maximum number:", max_num)
print("Minimum number:", min_num)
