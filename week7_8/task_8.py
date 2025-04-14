"""
Program: Perform addition, subtraction, multiplication, and division on two Pandas Series

"""

import pandas as pd

# Create two Pandas Series with three elements each
s1 = pd.Series([10, 20, 30])  # First series
s2 = pd.Series([1, 2, 3])     # Second series

# Perform element-wise arithmetic operations
# Addition: adds corresponding elements
print("Addition:\n", s1 + s2)

# Subtraction: subtracts corresponding elements
print("Subtraction:\n", s1 - s2)

# Multiplication: multiplies corresponding elements
print("Multiplication:\n", s1 * s2)

# Division: divides corresponding elements
print("Division:\n", s1 / s2)
