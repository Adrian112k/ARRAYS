import random

# arr1: Single-dimensional array with specified values
arr1 = [3, 7, 1, 0, 4]

# arr2: Two-dimensional array with specified values
arr2 = [[2, 3], [7, 1], [0, 4]]

# arr3: Array with 5 elements, each being 7
arr3 = [7 for i in range(5)]

# arr4: Array with integers from 1 to 9 (inclusive)
arr4 = [i for i in range(1, 10)]

# arr5: Array with multiples of 2 from 2 to 18 (inclusive)
arr5 = [i * 2 for i in range(1, 10)]

# arr6: Array with 10 random integers in the range of 1 to 20
arr6 = [random.randint(1, 20) for i in range(10)]

# arr7: Two-dimensional array with 5 empty lists
arr7 = [[] for i in range(5)]

# arr8: Two-dimensional array with 4 rows and 2 columns filled with 1
arr8 = [[1 for i in range(2)] for j in range(4)]

# arr9: Two-dimensional array with 5 rows and 3 columns filled with random integers in the range of 1 to 20
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# Array with values: 4, 0, 3
arr10 = [4, 0, 3]

# 15-element array filled with zeros
arr11 = [0] * 15

# Array with integer values in the range of <1, 30>
arr12 = [random.randint(1, 30) for i in range(10)]

# 20-element array filled with 0 or 1 randomly
arr13 = [random.choice([0, 1]) for i in range(20)]

# Two-dimensional array with 5 rows and 2 columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]

# Print the arrays
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)
print("arr5:", arr5)
print("arr6:", arr6)
print("arr7:", arr7)
print("arr8:", arr8)
print("arr9:", arr9)
print("arr10:", arr10)
print("arr11:", arr11)
print("arr12:", arr12)
print("arr13:", arr13)
print("arr14:", arr14)
