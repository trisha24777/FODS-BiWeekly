# Ask the user to input the first list of space-separated numbers and split the input into a list of strings
list1_str = input("Enter first list (space-separated numbers): ").split()

# Initialize an empty list to store integers
list1 = []

# Convert each string in the first list to an integer and append to list1
for item in list1_str:
    list1.append(int(item))

# Repeat the same process for the second list
list2_str = input("Enter second list (space-separated numbers): ").split()
list2 = []

# Convert each string in the second list to an integer and append to list2
for item in list2_str:
    list2.append(int(item))

# Compare if both lists have the same length
print("Same length:", len(list1) == len(list2))

# Compare if the sum of elements in both lists is equal
print("Same sum:", sum(list1) == sum(list2))

# Find and print the common elements between the two lists using set intersection
print("Common elements:", list(set(list1) & set(list2)))
