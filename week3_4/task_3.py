''' Function to check if a number is Armstrong '''
def is_armstrong(n):
    digits = str(n)
    length = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** length
    return total == n