"""
Program: Create a vector of size 10 with values from 0 to 1, excluding 0 and 1

This program creates a vector of 10 evenly spaced values between 0 and 1,
excluding the endpoints (0 and 1). It uses NumPy's linspace function to generate
the values and then removes the first and last elements.

The program:
1. Generates 12 evenly spaced points between 0 and 1
2. Removes the first (0) and last (1) values
3. Results in a vector of 10 values between 0 and 1

Author: [Your Name]
Date: [Current Date]
"""

import numpy as np

# Generate 12 evenly spaced points between 0 and 1, then remove first and last values
# This gives us 10 points between 0 and 1, excluding 0 and 1
vector = np.linspace(0, 1, 12)[1:-1]

# Display the resulting vector
print("Vector:", vector)
