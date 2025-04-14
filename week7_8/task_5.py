"""
Program: Create a 5x5 matrix with row values from 0 to 4

This program creates a 5x5 matrix where each row contains values from 0 to 4.
It uses NumPy's tile() function to repeat the sequence [0,1,2,3,4] five times
to create the desired matrix structure.

The program:
1. Creates a sequence of numbers from 0 to 4 using np.arange()
2. Uses np.tile() to repeat this sequence 5 times to form rows
3. Results in a 5x5 matrix where each row is [0,1,2,3,4]

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np

# Create a sequence from 0 to 4 and repeat it 5 times to form rows
# np.tile() repeats the input array the specified number of times
matrix = np.tile(np.arange(5), (5, 1))

# Display the resulting matrix
print("Matrix:\n", matrix)
