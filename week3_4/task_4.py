''' Function to sort a list of names '''

def sort_names(names):
    """
    Sorts a list of names in alphabetical order.

    This function takes a list of names and sorts them in ascending order
    using Python's built-in sort method. The sorting is case-sensitive
    and modifies the original list.

    Args:
        names (list): A list of strings containing names to be sorted.

    Returns:
        list: The sorted list of names.
    """
    names.sort()
    return names

names = ["Trisha", "Bhatta", "Ram", "Sham", "Hari"]
sorted_names = sort_names(names)
print("Sorted names: ", sorted_names)