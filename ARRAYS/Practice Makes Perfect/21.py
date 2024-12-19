# Function to check if the first array is a subset of the second array
def is_subset(array1, array2):
    # Iterate through all elements in array1
    for element in array1:
        # If an element in array1 is not found in array2, return False
        if element not in array2:
            return False
    # If all elements are found, return True
    return True

# Example arrays
array1 = [3, 5, 7]
array2 = [5, 7, 3, 9, 8, 1]

# Call the function and print the result
if is_subset(array1, array2):
    print(f"Array1: {array1} is a subset of Array2: {array2}")
else:
    print(f"Array1: {array1} is NOT a subset of Array2: {array2}")
