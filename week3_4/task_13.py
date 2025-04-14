def word_intersection():
    """Prompts the user for two English words and displays their common letters."""
    
    # Prompt the user for the first word and convert it to lowercase
    word1 = input("Enter the first word: ").lower()
    
    # Prompt the user for the second word and convert it to lowercase
    word2 = input("Enter the second word: ").lower()

    # Convert both words to sets to get the unique letters in each word
    set1 = set(word1)
    set2 = set(word2)

    # Find the intersection of the two sets to get the common letters
    common_letters = set1.intersection(set2)

    # Check if there are any common letters
    if common_letters:
        # If common letters exist, sort them alphabetically and display them
        print(f"The letters common to '{word1}' and '{word2}' are: {', '.join(sorted(list(common_letters)))}")
    else:
        # If no common letters exist, inform the user
        print(f"'{word1}' and '{word2}' have no letters in common.")

# Call the function to execute
word_intersection()
