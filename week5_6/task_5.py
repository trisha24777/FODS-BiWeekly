'''
This program counts the occurrence of each word in a text file.
'''
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
    word_counts = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.strip().lower()
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.split()
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    counts = count_word_occurrences(file_path)
    if counts:
        print("\nWord Occurrences:")
        for word, count in sorted(counts.items()):
            print(f"{word}: {count}")