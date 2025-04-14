"""
Program: Create, sort and reshape a random integer array

This program demonstrates NumPy array operations by:
1. Creating an array of random integers
2. Sorting the array in ascending order
3. Reshaping the array into a 2x5 matrix

The program shows how to generate random numbers, sort arrays,
and reshape them into different dimensions while maintaining the data.

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np

# Generate an array of 10 random integers between 1 and 100
arr = np.random.randint(1, 100, size=10)

# Sort the array in ascending order
arr.sort()

# Display the sorted array
print("Sorted Array:", arr)

# Reshape the array into a 2x5 matrix
# Note: The total number of elements must remain the same (10)
reshaped = arr.reshape(2, 5)

# Display the reshaped matrix
print("Reshaped Matrix (2x5):\n", reshaped)
