''' Function to check if a number is prime '''
def is_prime(n):
    """
    Checks if a given number is prime.

    This function determines if a number is prime by checking if it is
    divisible by any number from 2 up to its square root. Numbers less
    than 2 are considered not prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")