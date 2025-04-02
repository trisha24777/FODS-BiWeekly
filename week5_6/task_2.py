'''
This program copies the contents of a source file to a destination file.
'''
def copy_file(source_filepath, destination_filepath):
    """
    Copies the contents of the source file to the destination file.

    Args:
        source_filepath (str): The path to the source file.
        destination_filepath (str): The path to the destination file.

    Returns:
        bool: True if the copy was successful, False otherwise.
    """
    try:
        with open(source_filepath, 'r') as source_file:
            content = source_file.read()
        with open(destination_filepath, 'w') as destination_file:
            destination_file.write(content)
        print(f"Successfully copied contents from '{source_filepath}' to '{destination_filepath}'")
        return True
    except FileNotFoundError:
        print(f"Error: Source file not found at '{source_filepath}'")
        return False
    except Exception as e:
        print(f"An error occurred during file copying: {e}")
        return False

if __name__ == "__main__":
    source_path = input("Enter the path to the source file: ")
    destination_path = input("Enter the path to the destination file: ")
    copy_file(source_path, destination_path)