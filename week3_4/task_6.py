''' Program to store only values between 1-100 '''
numbers = []

# Process each number from the input
for x in input("Enter integers: ").split():
    # Convert string to integer
    num = int(x)
    # Check if number is within valid range (1-100)
    if 1 <= num <= 100:
        numbers.append(num)

# Display the filtered list
print("Filtered list:", numbers)