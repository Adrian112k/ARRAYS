# Funkcja sprawdzająca, czy liczba występuje w tablicy
def occurs(number, array):
    return number in array

# Tablica do sprawdzenia
array = [15, 38, 7, 23, 14]

# Wprowadzanie liczby z klawiatury
number = int(input("Enter a number: "))

# Wypisanie tablicy
print("Array:", " ".join(map(str, array)))

# Sprawdzenie, czy liczba występuje w tablicy
if occurs(number, array):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
