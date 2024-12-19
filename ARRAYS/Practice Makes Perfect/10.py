# Defining the two arrays
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# Loop through the first array and print the elements that are not in the second array
for num in array1:
    if num not in array2:
        print(num)
