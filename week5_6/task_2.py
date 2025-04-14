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
        # Open the source file in read mode ('r') to read its contents
        with open(source_filepath, 'r') as source_file:
            content = source_file.read()  # Read the entire content of the source file
        
        # Open the destination file in write mode ('w') to write the copied content
        with open(destination_filepath, 'w') as destination_file:
            destination_file.write(content)  # Write the content to the destination file
        
        # Print a success message if copying is successful
        print(f"Successfully copied contents from '{source_filepath}' to '{destination_filepath}'")
        
        # Return True indicating successful copy
        return True

    except FileNotFoundError:
        # Handle the case where the source file is not found
        print(f"Error: Source file not found at '{source_filepath}'")
        return False  # Return False indicating failure

    except Exception as e:
        # Handle any other unforeseen errors (e.g., permission issues)
        print(f"An error occurred during file copying: {e}")
        return False  # Return False indicating failure

# Main block to execute when the script is run directly
if __name__ == "__main__":
    # Prompt the user for the source file path
    source_path = input("Enter the path to the source file: ")
    
    # Prompt the user for the destination file path
    destination_path = input("Enter the path to the destination file: ")
    
    # Call the function to copy the file
    copy_file(source_path, destination_path)
