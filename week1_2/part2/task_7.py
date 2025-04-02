''' Program to count digits and letters in a string '''
string = input("Enter a string: ")
digits = sum(c.isdigit() for c in string)
letters = sum(c.isalpha() for c in string)
print("Digits:", digits)
print("Letters:", letters)