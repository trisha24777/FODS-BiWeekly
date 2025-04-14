'''
This program takes a text file as input and counts the number of lines, words, and characters in it.
'''

def analyze_file(filepath):
    """
    Counts the number of lines, words, and characters in a given text file.

    Args:
        filepath (str): The path to the text file.

    Returns:
        tuple: A tuple containing the number of lines, words, and characters.
               Returns None if the file cannot be opened.
    """
    try:
        # Attempt to open the file in read mode ('r')
        with open(filepath, 'r') as file:
            # Read all lines from the file into a list
            lines = file.readlines()
            
            # Count the number of lines in the file
            num_lines = len(lines)
            
            # Initialize counters for words and characters
            num_words = 0
            num_chars = 0
            
            # Loop through each line to count the characters and words
            for line in lines:
                num_chars += len(line)  # Add the number of characters in the line
                words = line.split()    # Split the line into words based on whitespace
                num_words += len(words)  # Add the number of words in the line
        
        # Return the results as a tuple (number of lines, words, and characters)
        return num_lines, num_words, num_chars

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File not found at '{filepath}'")
        return None
    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An error occurred: {e}")
        return None

# Main entry point of the program
if __name__ == "__main__":
    # Prompt the user to enter the file path
    file_path = input("Enter the path to the text file: ")
    
    # Call the function to analyze the file
    analysis = analyze_file(file_path)
    
    # If analysis was successful, display the results
    if analysis:
        num_lines, num_words, num_chars = analysis
        print(f"\nAnalysis of '{file_path}':")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
