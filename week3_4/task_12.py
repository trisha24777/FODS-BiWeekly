set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# (a) Union of sets
union_set = set1.union(set2)
print(f"(a) Union of set1 and set2: {union_set}")
print(f"Length of the union set: {len(union_set)}")

# (b) Intersection of sets
intersection_set = set1.intersection(set2)
print(f"(b) Intersection of set1 and set2: {intersection_set}")

# (c) Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(f"(c) Symmetric difference of set1 and set2: {symmetric_difference_set}")

# (d) Add the value 40 to set1
original_length = len(set1)
set1.add(40)
new_length = len(set1)
print(f"(d) set1 after adding 40: {set1}")
if new_length > original_length:
    print("The set changed.")
else:
    print("The set did not change (40 was already present).")

# (e) Remove value 20 from set2
set2.discard(20)  # Using discard to avoid KeyError if 20 isn't present
print(f"(e) set2 after removing 20: {set2}")