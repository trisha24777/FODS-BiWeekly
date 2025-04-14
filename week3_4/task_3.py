''' Function to check if a number is Armstrong '''
def is_armstrong(n):
    """
    Checks if a given number is an Armstrong number.

    An Armstrong number is a number that equals the sum of its own digits
    raised to the power of the number of digits. For example, 153 is an
    Armstrong number because 1^3 + 5^3 + 3^3 = 153.

    Args:
        n (int): The number to check for Armstrong property.

    Returns:
        bool: True if the number is Armstrong, False otherwise.
    """
    digits = str(n)
    length = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** length
    return total == n  

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")