import numpy as np

# Creating a 3x3 matrix with random values
matrix = np.random.rand(3, 3)
print("Initial matrix:\n", matrix)

# Adding values to matrix elements
matrix += 5
print("Matrix after adding 5 to each element:\n", matrix)

# Multiplying the matrix by a scalar
matrix *= 2
print("Matrix after multiplying each element by 2:\n", matrix)

# Transposing the matrix
matrix = matrix.T
print("Matrix after transposition:\n", matrix)

# Inverting the matrix
matrix_inv = np.linalg.inv(matrix)
print("Inverted matrix:\n", matrix_inv)

# Multiplying two matrices
matrix2 = np.random.rand(3, 3)
print("Second matrix:\n", matrix2)
matrix_result = np.dot(matrix, matrix2)
print("Result of multiplying two matrices:\n", matrix_result)

# Displaying the sum of elements in the matrix
matrix_sum = np.sum(matrix)
print("Sum of elements in the matrix:", matrix_sum)

# Displaying the mean value of elements in the matrix
matrix_mean = np.mean(matrix)
print("Mean value of elements in the matrix:", matrix_mean)
