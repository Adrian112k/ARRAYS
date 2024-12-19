# Funkcja, która zwraca drugi największy element w tablicy
def second_largest(arr):
    arr_sorted = sorted(arr, reverse=True)  # Sortujemy tablicę malejąco
    return arr_sorted[1]  # Zwracamy drugi element

# Funkcja, która zwraca różnicę między największym a najmniejszym elementem w tablicy
def difference_between_largest_and_smallest(arr):
    largest = max(arr)
    smallest = min(arr)
    return largest - smallest

# Funkcja, która zwraca medianę liczb w tablicy
def median(arr):
    arr_sorted = sorted(arr)  # Sortujemy tablicę rosnąco
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]  # Jeżeli liczba elementów jest nieparzysta, zwracamy środkowy element
    else:
        # Jeżeli liczba elementów jest parzysta, zwracamy średnią z dwóch środkowych elementów
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2

# Funkcja, która zwraca najmniejszy i największy element w tablicy jako krotkę
def smallest_and_largest(arr):
    return (min(arr), max(arr))

# Funkcja, która zwraca elementy tablicy jako ciąg znaków, rozdzielony myślnikiem
def array_as_string(arr):
    return '-'.join(map(str, arr))
