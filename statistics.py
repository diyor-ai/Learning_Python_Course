import numpy as np
""" 
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Calculate statistics
print("Mean:", np.mean(data)) # 5.0
print("Median:", np.median(data)) # 5.0
print("Std:", np.std(data)) # ~2.58
print("Min/Max:", np.min(data), np.max(data))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Matrix Multiplication
product = A @ B # or np.dot(A, B)
# Transpose
transpose_A = A.T
# Determinant & Inverse
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print("Transpose:\n", transpose_A)
print("Inverse:\n", inv_A)

matrix = np.random.rand(3,3)
print(matrix)
print(np.mean(matrix,axis=1))
print(np.median(matrix))
print(np.std(matrix))
print(np.min(matrix))
print(np.max(matrix))
"""
import numpy as np

# Create matrices using np.array()
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Matrix multiplication using @ operator
product_1 = A @ B
print("\nMatrix Multiplication (A @ B):")
print(product_1)

# Matrix multiplication using np.dot()
product_2 = np.dot(A, B)
print("\nMatrix Multiplication (np.dot(A, B)):")
print(product_2)

# Find the inverse of matrix A using np.linalg.inv()
inverse_A = np.linalg.inv(A)
print("\nInverse of Matrix A:")
print(inverse_A)

# Verify: A * A^(-1) should give identity matrix
identity = A @ inverse_A
print("\nVerification (A @ A^(-1)) - should be identity matrix:")
print(identity)

# Additional: Determinant
det_A = np.linalg.det(A)
print(f"\nDeterminant of A: {det_A}")