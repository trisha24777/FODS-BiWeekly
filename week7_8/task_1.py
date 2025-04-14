"""
Program: Create a null vector of size 10 with the fifth value as 1

This program demonstrates the creation of a null vector (vector of zeros) using NumPy
and then modifies a specific element to create a unit vector with a single non-zero element.

The program:
1. Creates a vector of size 10 filled with zeros
2. Sets the fifth element (index 4) to 1
3. Prints the resulting vector

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np

# Create a vector of zeros with size 10
vector = np.zeros(10)

# Set the fifth element (index 4) to 1
# Note: In Python, indexing starts at 0, so the fifth element is at index 4
vector[4] = 1

# Display the resulting vector
print("Resultant Vector:", vector)
