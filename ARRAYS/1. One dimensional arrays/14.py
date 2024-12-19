# Implementacja algorytmu sortowania bąbelkowego
def bubbleSort(arr):
    n = len(arr)
    
    # Przechodzimy przez wszystkie elementy tablicy
    for i in range(n):
        # Ostatnie i elementy są już posortowane, więc nie musimy ich porównywać
        for j in range(0, n-i-1):
            # Zamieniamy miejscami, jeśli element jest większy od następnego
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Zamiana miejscami elementów
    
    return arr

# Przykład użycia
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubbleSort(arr)
print("Posortowana tablica:", sorted_arr)
