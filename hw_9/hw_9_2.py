from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Calculates the difference between the maximum and minimum values among the passed numbers.
    If there are no arguments, returns 0.

    Args:
        *args (Union[int, float]): Variable number of arguments of numeric type.

    Returns:
        Union[int, float]: The difference between the maximum and minimum.
        Returns 0 if there are no arguments.

    Example:
        >>> difference(1, 2, 3)
        2
        >>> difference(5, -5)
        10
        >>> difference(10.2, -2.2, 0, 1.1, 0.5)
        12.4
        >>> difference()
        0
    """

    # If there are no arguments, return 0.
    if not args:
        return 0

    return round(max(args) - min(args), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'

print('OK')
