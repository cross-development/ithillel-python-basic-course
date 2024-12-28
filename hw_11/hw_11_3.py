def is_even(number: int) -> bool:
    """
    Determines if a number is even without using division-related operations.

    Args:
        number: The number to check.

    Returns:
        True if the number is even, False otherwise.
    """

    # The bitwise AND operator (&) with 1 checks the least significant bit of the number:
    # - If the least significant bit is 0, the number is even.
    # - If the least significant bit is 1, the number is odd.
    # This works because even numbers in binary always end with 0, and odd numbers end with 1.
    # Ref: https://stackoverflow.com/a/160942
    return (number & 1) == 0


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'

print('Ok')
