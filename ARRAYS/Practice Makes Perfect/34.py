# Function to create an identity matrix of size n
def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = [1 if i == j else 0 for j in range(n)]
        matrix.append(row)
    return matrix

# Function to print the 2D matrix in rows and columns
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Create and print identity matrices of sizes 3, 5, and 8
sizes = [3, 5, 8]

for size in sizes:
    print(f"Identity Matrix of size {size}:")
    matrix = identity_matrix(size)
    print_matrix(matrix)
    print()  # Add a newline between matrices
