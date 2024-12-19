# Function to flatten 2D array to 1D
def flatten_2d_to_1d(array_2d):
    # Flatten the 2D array by iterating over each row and element
    return [item for row in array_2d for item in row]

# Define 2D arrays
array1 = [
    [2, 3],
    [1, 5]
]

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Convert each 2D array to 1D and print the result
arrays = [array1, array2, array3]
for idx, array in enumerate(arrays, 1):
    print(f"2D Array {idx}:")
    for row in array:
        print(row)
    flattened = flatten_2d_to_1d(array)
    print(f"1D Array {idx}: {flattened}")
    print()  # Add a newline between array prints
