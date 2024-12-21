from inspect import isgenerator
from typing import Generator, Callable


def pow(x: int) -> int:
    """
    Calculates the square of a number.

    Args:
        x: The number to be squared.

    Returns:
        The square of the input number.
    """
    return x ** 2


def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Generator[int, None, None]:
    """
    Generate a sequence based on a user-defined function.

    Args:
        begin: The first element of the sequence.
        end: The number of elements in the sequence.
        func: A function that generates the value for the sequence.

    Returns:
        Elements of the sequence.
    """
    current = begin

    for _ in range(end):
        yield current

        current = func(current)


gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
