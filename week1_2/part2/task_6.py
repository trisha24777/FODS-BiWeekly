''' Program to find numbers divisible by 7 and multiple of 5 between 1500 and 2000 '''
for num in range(1500, 2001):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")
print()