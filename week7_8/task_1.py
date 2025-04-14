"""
Program: Create a null vector of size 10 with the fifth value as 1

"""

import numpy as np

# Create a vector of zeros with size 10
vector = np.zeros(10)

# Set the fifth element (index 4) to 1
# Note: In Python, indexing starts at 0, so the fifth element is at index 4
vector[4] = 1

# Display the resulting vector
print("Resultant Vector:", vector)
