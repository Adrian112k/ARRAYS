# Initial square matrix
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Replacing the main diagonal values with 1
for i in range(len(matrix)):
   matrix[i][i] = 1

# Printing the modified matrix
for row in matrix:
   print(" ".join(map(str, row)))
