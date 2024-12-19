# Tablica zawierająca liczby całkowite
numbers = [34, 7, 19, 4, 21, 8]

# Inicjalizacja licznika liczb parzystych
even_count = 0
i = 0

# Pętla 'while' przechodząca przez tablicę
while i < len(numbers):
    if numbers[i] % 2 == 0:  # Sprawdzanie, czy liczba jest parzysta
        even_count += 1
    i += 1

# Wypisanie liczby liczb parzystych
print("Liczba liczb parzystych:", even_count)
