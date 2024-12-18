def common_elements() -> set:
    """
    Finds the common elements between multiples of 3 and multiples of 5 within a range of 0 to 99.

    This function generates two sets:
    - Numbers that are multiples of 3 within the range [0, 99].
    - Numbers that are multiples of 5 within the same range.

    It then computes and returns the intersection of these two sets, which includes numbers that
    are divisible by both 3 and 5 (i.e., multiples of 15).

    Returns:
        set: A set of integers that are common to both multiples of 3 and multiples of 5.

    Example:
        >>> common_elements()
        {0, 15, 30, 45, 60, 75, 90}
    """

    # Create a list of numbers that are multiples of 3
    multiples_of_three = set(x for x in range(100) if x % 3 == 0)

    # Create a list of numbers that are multiples of 5
    multiples_of_five = set(x for x in range(100) if x % 5 == 0)

    # Find the intersection of sets
    common = multiples_of_three.intersection(multiples_of_five)

    return common


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test1'

print('ОК')
