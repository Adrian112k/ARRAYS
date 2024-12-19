###
# Modifies array values step by step
#
arr = [1, 2, 3, 4, 5]

print('Array:', arr)  # Początkowa tablica

# Odejmij 1 od pierwszego elementu
arr[0] -= 1
print('Array:', arr)  # Po zmianie pierwszego elementu

# Zwiększ ostatni element tablicy o 4
arr[len(arr) - 1] += 4
print('Array:', arr)  # Po zmianie ostatniego elementu

# Pomnóż środkowy element przez 2
middle_index = len(arr) // 2
arr[middle_index] *= 2
print('Array:', arr)  # Po zmianie środkowego elementu
