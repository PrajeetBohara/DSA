def merge_sort(list):
    """Sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublists created in previous step
    Merge the sorted sublists created in previous step"""

    if len(list)