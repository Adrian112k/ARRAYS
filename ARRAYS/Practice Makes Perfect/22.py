import random

# Function to return a randomly selected element from the array
def rand_elem(array):
    return random.choice(array)

# Example array
my_array = [10, 20, 30, 40, 50]

# Print a few randomly selected elements from the array
print("Randomly selected elements:")
for _ in range(5):  # Selecting 5 random elements as an example
    print(rand_elem(my_array))
