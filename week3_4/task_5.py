''' Calculator functions '''

def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (float/int): First number.
        b (float/int): Second number.

    Returns:
        float/int: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (float/int): First number.
        b (float/int): Second number.

    Returns:
        float/int: The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers together.

    Args:
        a (float/int): First number.
        b (float/int): Second number.

    Returns:
        float/int: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second, rounding to 2 decimal places.

    Args:
        a (float/int): First number (dividend).
        b (float/int): Second number (divisor).

    Returns:
        float: The quotient of a divided by b, rounded to 2 decimal places.
    """
    return round(a / b, 2)

def truncated_div(a, b):
    """
    Performs integer division (truncated division) of two numbers.

    Args:
        a (float/int): First number (dividend).
        b (float/int): Second number (divisor).

    Returns:
        int: The truncated quotient of a divided by b.
    """
    return a // b

def modulus(a, b):
    """
    Calculates the remainder when the first number is divided by the second.

    Args:
        a (float/int): First number (dividend).
        b (float/int): Second number (divisor).

    Returns:
        float/int: The remainder of a divided by b.
    """
    return a % b

def exponentiate(a, b):
    """
    Raises the first number to the power of the second number.

    Args:
        a (float/int): Base number.
        b (float/int): Exponent.

    Returns:
        float/int: a raised to the power of b.
    """
    return a ** b


def main():
    print("Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Truncated Division")
    print("6. Modulus")
    print("7. Exponentiation")
    print("8. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 8:
        print("Exiting the program...")
        return
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    elif choice == 5:
        result = truncated_div(num1, num2)
    elif choice == 6:
        result = modulus(num1, num2)
    elif choice == 7:
        result = exponentiate(num1, num2)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    