''' Program to store only values between 1-100 '''
numbers = []
for x in input("Enter integers: ").split():
    num = int(x)
    if 1 <= num <= 100:
        numbers.append(num)
print("Filtered list:", numbers)