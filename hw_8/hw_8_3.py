def find_unique_value(some_list: list[int]) -> int | float:
    """
    Find the first unique value in a list of integers.

    This function returns the first element in the list that appears only once. If multiple unique
    values exist, it returns the one that appears first. The function assumes that there is at least
    one unique element in the list.

    Args:
        some_list (list[int]): A list of integers where the function searches for the first unique value.

    Returns:
        int | float: The first unique value in the list. The return type is either an integer or a float.

    Example:
        >>> find_unique_value([1, 2, 1, 1])
        2
        >>> find_unique_value([2, 3, 3, 3, 5, 5])
        2
        >>> find_unique_value([5, 5, 5, 2, 2, 0.5])
        0.5
    """

    return [x for x in some_list if some_list.count(x) == 1][0]


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")
