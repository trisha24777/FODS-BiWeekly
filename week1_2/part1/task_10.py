'''Finds Unicode encoding of each character in the name'''
name = "Trisha"  
unicode_values = [ord(char) for char in name]
print("The unicode incoing is: ",unicode_values)
