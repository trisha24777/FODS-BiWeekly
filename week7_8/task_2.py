"""
Program: Generate a random array with user-defined shape and calculate average

"""

import numpy as np

# Get array dimensions from user
a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))

# Generate random array with values between 0 and 1
array = np.random.rand(a, b)

# Display the generated array
print("Random Array:\n", array)

# Calculate and display the average of all elements
print("Average of Array:", np.mean(array))
