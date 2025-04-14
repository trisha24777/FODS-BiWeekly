''' Function to count uppercase and lowercase letters in a string '''
def count_case(s):
    """
    Counts the number of uppercase and lowercase letters in a string.

    This function iterates through each character in the input string and
    keeps track of how many uppercase and lowercase letters are found.

    Args:
        s (str): The input string to analyze.

    Returns:
        tuple: A tuple containing two integers:
            - First integer: count of uppercase letters
            - Second integer: count of lowercase letters
    """
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    return upper, lower

word = "My Nmae is Trisha Bhatta"
upper, lower = count_case(word)
print("Counts in ", word)
print("Uppercase count: ", upper)
print("Lowercase count: ", lower)