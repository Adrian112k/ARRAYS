# Tablica zawierająca liczby
numbers = [15, 8, 31, 47, 2, 19]

# Obliczanie sumy elementów w tablicy
sum_numbers = 0
for num in numbers:
    sum_numbers += num

# Obliczanie średniej arytmetycznej
mean = sum_numbers / len(numbers)

# Wypisanie tablicy oraz średniej arytmetycznej
print("Array:", *numbers)
print("Arithmetic mean:", mean)
