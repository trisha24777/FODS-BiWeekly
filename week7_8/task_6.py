"""
Program: Take user input array, sort and perform slicing

"""

import numpy as np

# Get user input and convert to NumPy array
# Split the input string by spaces and convert each element to integer
user_input = input("Enter at least 10 integers separated by spaces: ")
arr = np.array(list(map(int, user_input.split())))

# Sort the array in ascending order
arr.sort()

# Display the sorted array
print("Sorted Array:", arr)

# Demonstrate different slicing operations
# Note: Slicing syntax is [start:end] where end is exclusive
print("Elements from index 2 to 5:", arr[2:6])  # Gets elements at indices 2,3,4,5
print("Elements from index 5 to 8:", arr[5:9])  # Gets elements at indices 5,6,7,8
print("Elements from index 2 to 9:", arr[2:10])  # Gets elements at indices 2 through 9
