def is_even(digit: int) -> bool:
    """
    Checks if a given integer is even.

    Args:
        digit: The integer to be checked.

    Returns:
        True if the digit is even, False otherwise.
    """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'

print('OK')