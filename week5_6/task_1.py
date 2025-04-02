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
        with open(filepath, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = 0
            num_chars = 0
            for line in lines:
                num_chars += len(line)
                words = line.split()
                num_words += len(words)
        return num_lines, num_words, num_chars
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    analysis = analyze_file(file_path)
    if analysis:
        num_lines, num_words, num_chars = analysis
        print(f"\nAnalysis of '{file_path}':")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")