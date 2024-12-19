# Tablica zawierająca liczby
numbers = [15, 8, 31, 47, 2, 19]

# Inicjalizacja zmiennych do sumowania i liczenia elementów
sum_numbers = 0
index = 0

# Pętla while przechodząca przez tablicę
while index < len(numbers):
    sum_numbers += numbers[index]
    index += 1

# Obliczanie średniej arytmetycznej
mean = sum_numbers / len(numbers)

# Wypisanie tablicy oraz średniej arytmetycznej
print("Array:", *numbers)
print("Arithmetic mean:", mean)
