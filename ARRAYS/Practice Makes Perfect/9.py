# Funkcja porównująca dwa array'e
def compare(array1, array2):
    # Sprawdzamy, czy długości tablic są równe i porównujemy je element po elemencie
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

# Testowe tablice
array1_1 = ["water", "book", "sky"]
array2_1 = ["water", "book", "sky"]

array1_2 = [True, False]
array2_2 = [True, False, True]

array1_3 = [5, 3, 1]
array2_3 = [5, 3, 1]

array1_4 = [3, 2, 1]
array2_4 = [3, 2]

# Testowanie porównania
arrays = [
    (array1_1, array2_1),
    (array1_2, array2_2),
    (array1_3, array2_3),
    (array1_4, array2_4)
]

# Pętla sprawdzająca każdą parę tablic
for i, (arr1, arr2) in enumerate(arrays, 1):
    print(f"Array{i}:", *arr1)
    print(f"Array{i+1}:", *arr2)
    result = "arrays are the same" if compare(arr1, arr2) else "arrays are different"
    print(f"Comparison: {result}\n")
