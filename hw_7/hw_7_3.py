def second_index(text: str, some_str: str) -> int | None:
    """
    Finds the second occurrence of a given substring in the provided text.

    This function searches for the first occurrence of the substring `some_str`
    in the input string `text`. If a second occurrence exists, it returns the
    starting index of that occurrence. If the substring does not occur twice,
    the function returns None.

    Args:
        text (str): The input string in which to search for the substring.
        some_str (str): The substring to search for in the text.

    Returns:
        int | None: The starting index of the second occurrence of `some_str`
                    in `text`. Returns None if there is no second occurrence.

    Examples:
        >>> second_index("sims", "s")
        3
        >>> second_index("find the river", "e")
        12
        >>> second_index("hi", "h")
        None
        >>> second_index("Hello, hello", "lo")
        10
    """

    # Find the first occurrence
    first = text.find(some_str)

    # If there is no first occurrence, return None
    if first == -1:
        return None

    # We are looking for the second occurrence, starting after the first
    # Add the length of the search string to avoid finding the same occurrence
    second = text.find(some_str, first + len(some_str))

    # If there is no second occurrence, return None
    if second == -1:
        return None

    return second


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')
