"""
Program: Create a vector of size 10 with values from 0 to 1, excluding 0 and 1

"""

import numpy as np

# Generate 12 evenly spaced points between 0 and 1, then remove first and last values
# This gives us 10 points between 0 and 1, excluding 0 and 1
vector = np.linspace(0, 1, 12)[1:-1]

# Display the resulting vector
print("Vector:", vector)
