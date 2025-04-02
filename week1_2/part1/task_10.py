'''Finds Unicode encoding of each character in the name'''
name = "Trisha"  
unicode_values = [ord(char) for char in name]
print(unicode_values)
