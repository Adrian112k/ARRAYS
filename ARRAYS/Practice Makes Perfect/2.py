# Tablica zawierająca liczby naturalne
numbers = [15, 8, 31, 47, 2, 19]

# Wypisanie oryginalnej tablicy
print("existed array:", end=" ")
for num in numbers:
    print(num, end=" ")

# Wypisanie tablicy w odwrotnej kolejności
print("\nreverse array:", end=" ")
for num in reversed(numbers):
    print(num, end=" ")
