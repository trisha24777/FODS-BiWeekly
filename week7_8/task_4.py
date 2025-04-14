"""
Program: Check if a (3,4) identity matrix is possible and print result

This program demonstrates the creation of an identity-like matrix with non-square dimensions.
While a true identity matrix must be square (same number of rows and columns), NumPy's eye()
function can create a matrix with identity-like properties for rectangular dimensions.

The program:
1. Creates a 3x4 matrix using np.eye()
2. The resulting matrix has 1's on the main diagonal (where possible)
3. Demonstrates that while not a true identity matrix, we can create
   a matrix with identity-like properties for rectangular dimensions

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np

# Create a 3x4 matrix with identity-like structure
# Note: A true identity matrix must be square, but np.eye() can create
# a rectangular matrix with 1's on the main diagonal where possible
identity_like = np.eye(3, 4)

# Display the resulting matrix
print("3x4 Identity-like matrix:\n", identity_like)
