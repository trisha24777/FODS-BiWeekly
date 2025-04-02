''' Count occurrences of 'a' in list of names '''
names = input("Enter names separated by space: ").split()
count_a = 0
for name in names:
    count_a += name.lower().count('a')
print("Occurrences of 'a':", count_a)