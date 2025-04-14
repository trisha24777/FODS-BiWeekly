'''
This program counts the occurrence of each word in a text file.
'''

# Importing the string module to handle punctuation
import string

def count_word_occurrences(filepath):
    """
    Counts the occurrences of each word in a given text file.

    Args:
        filepath (str): The path to the text file.

    Returns:
        dict: A dictionary where keys are words (lowercase) and values are their counts.
              Returns None if the file cannot be opened.
    """
    # Initialize an empty dictionary to store word counts
    word_counts = {}

    try:
        # Open the file in read mode
        with open(filepath, 'r') as file:
            # Loop through each line in the file
            for line in file:
                # Remove leading/trailing whitespace and convert the line to lowercase
                line = line.strip().lower()

                # Remove punctuation from the line
                line = line.translate(str.maketrans('', '', string.punctuation))

                # Split the line into words based on whitespace
                words = line.split()

                # Loop through each word and count its occurrences
                for word in words:
                    # Update the word count in the dictionary
                    word_counts[word] = word_counts.get(word, 0) + 1

        # Return the dictionary of word counts
        return word_counts

    except FileNotFoundError:
        # Handle the case where the file cannot be found
        print(f"Error: File not found at '{filepath}'")
        return None  # Return None if the file cannot be found

    except Exception as e:
        # Handle any other unexpected errors (e.g., permission issues)
        print(f"An error occurred: {e}")
        return None  # Return None if an error occurs

# Main block that runs when the script is executed
if __name__ == "__main__":
    # Prompt the user for the path to the text file
    file_path = input("Enter the path to the text file: ")

    # Call the function to count word occurrences
    counts = count_word_occurrences(file_path)

    # If word counts are returned, print them
    if counts:
        print("\nWord Occurrences:")
        # Sort the word counts alphabetically and print each word with its count
        for word, count in sorted(counts.items()):
            print(f"{word}: {count}")
