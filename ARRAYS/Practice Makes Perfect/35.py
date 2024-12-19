# Function to transpose a matrix
def transpose_matrix(m):
    # Transpose by swapping rows and columns
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Original matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]

# Create and print transposed matrices
matrices = [matrix1, matrix2, matrix3]
for idx, matrix in enumerate(matrices, 1):
    print(f"Original Matrix {idx}:")
    print_matrix(matrix)
    transposed = transpose_matrix(matrix)
    print(f"Transposed Matrix {idx}:")
    print_matrix(transposed)
    print()  # Add a newline between matrix prints
