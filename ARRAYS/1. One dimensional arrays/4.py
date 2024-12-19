###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))  # Liczba elementów w tablicy
print('First value', arr[0])  # Pierwszy element (indeks 0)
print('Second value', arr[1])  # Drugi element (indeks 1)
print('Last value', arr[len(arr) - 1])  # Ostatni element (indeks długość - 1)
print('Last but one value', arr[len(arr) - 2])  # Przedostatni element (długość - 2)
print('Sum of the first and last value', arr[0] + arr[len(arr) - 1])  # Suma pierwszego i ostatniego elementu
print('Middle value', arr[len(arr) // 2])  # Środkowy element (długość podzielona przez 2)

# Wszystkie elementy tablicy, rozdzielone spacjami
print('All values:', end=' ')
for value in arr:
    print(value, end=' ')  # Iteracja przez tablicę i wypisywanie elementów
print()
