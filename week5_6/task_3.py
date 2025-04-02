'''
This program finds and replaces a specific word in a text file with another word.
'''
def find_and_replace(filepath, old_word, new_word):
    """
    Finds all occurrences of an old word in a file and replaces them with a new word.

    Args:
        filepath (str): The path to the text file.
        old_word (str): The word to be replaced.
        new_word (str): The word to replace with.

    Returns:
        bool: True if the replacement was successful, False otherwise.
    """
    try:
        with open(filepath, 'r+') as file:
            content = file.read()
            new_content = content.replace(old_word, new_word)
            file.seek(0)  # Go back to the beginning of the file
            file.write(new_content)
            file.truncate()  # Remove any remaining part of the old content
        print(f"Successfully replaced '{old_word}' with '{new_word}' in '{filepath}'")
        return True
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return False
    except Exception as e:
        print(f"An error occurred during find and replace: {e}")
        return False

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the new word: ")
    find_and_replace(file_path, word_to_replace, replacement_word)