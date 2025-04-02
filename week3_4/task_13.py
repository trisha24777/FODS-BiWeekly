def word_intersection():
    """Prompts the user for two English words and displays their common letters."""
    word1 = input("Enter the first word: ").lower()
    word2 = input("Enter the second word: ").lower()

    set1 = set(word1)
    set2 = set(word2)

    common_letters = set1.intersection(set2)

    if common_letters:
        print(f"The letters common to '{word1}' and '{word2}' are: {', '.join(sorted(list(common_letters)))}")
    else:
        print(f"'{word1}' and '{word2}' have no letters in common.")

word_intersection()