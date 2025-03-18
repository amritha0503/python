# Get matrix dimensions
n = int(input("Enter the size of square matrix (n x n): "))

# Input matrix elements
print(f"\nEnter {n*n} elements:")
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

# Display original matrix
print("\nOriginal Matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Rotate matrix 90 degrees clockwise
# First transpose the matrix
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Then reverse each row
for i in range(n):
    matrix[i] = matrix[i][::-1]

# Display rotated matrix
print("\nMatrix after 90 degree rotation:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()