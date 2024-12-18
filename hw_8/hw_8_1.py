def add_one(some_list: list[int]) -> list[int]:
    """
    Adds 1 to the number represented by a list of digits and returns the result as a new list of digits.

    Args:
        some_list (list[int]): A list of integers, where each integer is a single digit
                               (0-9), representing a number in order.

    Returns:
        list[int]: A list of integers representing the number after adding 1.

    Example:
        >>> add_one([1, 2, 3, 4])
        [1, 2, 3, 5]
        >>> add_one([9, 9, 9])
        [1, 0, 0, 0]
        >>> add_one([0])
        [1]
        >>> add_one([9])
        [1, 0]

    Notes:
        - The input list must contain only non-negative single-digit integers.
        - Handles carry-over correctly when the input represents a number ending in 9 or all 9s.
    """

    # Convert a list of digits to a single number and add 1 to the number
    number = int(''.join(map(str, some_list))) + 1

    # Convert the number back to a list of digits
    return [int(digit) for digit in str(number)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
