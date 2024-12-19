# Program do wypisania unikalnych elementów w tablicy
def unique_elements(arr):
    # Tworzymy słownik do przechowywania liczby wystąpień każdego elementu
    element_count = {}
    
    # Zliczamy wystąpienia każdego elementu
    for elem in arr:
        if elem in element_count:
            element_count[elem] += 1
        else:
            element_count[elem] = 1
    
    # Zbieramy te elementy, które występują dokładnie raz
    unique = [elem for elem, count in element_count.items() if count == 1]
    
    return unique

# Przykładowa tablica
array = [2, 3, 2, 5, 8, 1, 9, 8]

# Wypisanie wyników
print("Array:", " ".join(map(str, array)))
unique = unique_elements(array)
print("Unique elements:", " ".join(map(str, unique)))
