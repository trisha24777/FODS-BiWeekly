dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# (a) Concatenate dictionaries
nums = dic1.copy()
nums.update(dic2)
nums.update(dic3)
print(f"(a) Concatenated dictionary (nums): {nums}")

# (b) Add a new key/value pair
nums[7] = 70
print(f"(b) Dictionary with new item: {nums}")

# (c) Update the value of key 3
nums[3] = 80
print(f"(c) Dictionary with updated value for key 3: {nums}")

# (d) Remove the third item (key-value pair)
# Dictionaries are unordered before Python 3.7, so "third item" is ambiguous.
# Assuming you mean the item with the third key we added (key 5):
if 5 in nums:
    del nums[5]
    print(f"(d) Dictionary after removing key 5: {nums}")
else:
    print("(d) Key 5 not found in the dictionary.")

# (e) Sum all the items (values) in the dictionary
sum_of_values = sum(nums.values())
print(f"(e) Sum of all values in nums: {sum_of_values}")

# (f) Multiply all the items (values) in the dictionary
product_of_values = 1
for value in nums.values():
    product_of_values *= value
print(f"(f) Product of all values in nums: {product_of_values}")

# (g) Retrieve the maximum and minimum values
if nums:
    max_value = max(nums.values())
    min_value = min(nums.values())
    print(f"(g) Maximum value in nums: {max_value}")
    print(f"(g) Minimum value in nums: {min_value}")
else:
    print("(g) The dictionary 'nums' is empty.")
