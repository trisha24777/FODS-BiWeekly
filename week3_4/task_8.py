list1_str = input("Enter first list (space-separated numbers): ").split()
list1 = []
for item in list1_str:
    list1.append(int(item))

list2_str = input("Enter second list (space-separated numbers): ").split()
list2 = []
for item in list2_str:
    list2.append(int(item))

print("Same length:", len(list1) == len(list2))
print("Same sum:", sum(list1) == sum(list2))
print("Common elements:", list(set(list1) & set(list2)))