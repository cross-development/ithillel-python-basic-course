def second_index(text: str, some_str: str) -> int | None:
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
