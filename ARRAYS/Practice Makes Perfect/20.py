# Function to separate even and odd numbers
def separate_even_odd(arr):
    even_numbers = []
    odd_numbers = []

    # Iterate through the array
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)  # Add even numbers to even list
        else:
            odd_numbers.append(num)   # Add odd numbers to odd list

    # Concatenate even and odd lists
    return even_numbers + odd_numbers

# Given array of integers
arr = [7, 9, 2, 4, 5, 6]

# Call the function and get the result
arr = separate_even_odd(arr)

# Print the result
print("arr =", arr)
