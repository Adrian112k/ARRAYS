# Funkcja Bubble Sort
def bubblesort(array):
    n = len(array)
    # Przechodzimy przez wszystkie elementy tablicy
    for i in range(n):
        # Ostatnie i elementy są już posortowane
        for j in range(0, n-i-1):
            # Porównujemy sąsiednie elementy
            if array[j] > array[j+1]:
                # Zamieniamy miejscami, jeśli elementy są w złej kolejności
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Przykładowe tablice
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36, 10, 7]
array3 = [33, 8, 2, 19, 50, 13]

# Sortowanie tablic
sorted_array1 = bubblesort(array1)
sorted_array2 = bubblesort(array2)
sorted_array3 = bubblesort(array3)

# Drukowanie wyników
print("Posortowana tablica 1:", sorted_array1)
print("Posortowana tablica 2:", sorted_array2)
print("Posortowana tablica 3:", sorted_array3)
