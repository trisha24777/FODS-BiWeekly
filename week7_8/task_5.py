"""
Program: Create a 5x5 matrix with row values from 0 to 4

"""

import numpy as np

# Create a sequence from 0 to 4 and repeat it 5 times to form rows
# np.tile() repeats the input array the specified number of times
matrix = np.tile(np.arange(5), (5, 1))

# Display the resulting matrix
print("Matrix:\n", matrix)
