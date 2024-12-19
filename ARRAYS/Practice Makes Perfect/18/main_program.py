# Importowanie modułu MyArrays
import MyArrays

# Dana sekwencja liczb
numbers = [7, 3, 8, 5, 2]

# Drukowanie liczb
print("Numbers:", MyArrays.array_as_string(numbers))

# Drugi największy element
second_largest_num = MyArrays.second_largest(numbers)
print("Second largest number:", second_largest_num)

# Mediana
median_value = MyArrays.median(numbers)
print("Median:", median_value)

# Najmniejsza i największa liczba
smallest_largest = MyArrays.smallest_and_largest(numbers)
print(f"Smallest and largest number: {smallest_largest[0]},{smallest_largest[1]}")

# Różnica pomiędzy największą a najmniejszą liczbą
diff_largest_smallest = MyArrays.difference_between_largest_and_smallest(numbers)
print("Difference between largest and smallest number:", diff_largest_smallest)
