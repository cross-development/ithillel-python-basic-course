from inspect import isgenerator
from typing import Generator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    """
    Generate cubes of numbers starting from 2 up to the specified upper limit (inclusive).

    Args:
        end: The upper limit (inclusive) for generating cube numbers.

    Yields:
        The next cube of a number in the range from 2 onwards, which is less than or equal to `end`.
    """

    number = 2

    # An assignment expression (sometimes also called a “walrus”) assigns an expression to an identifier,
    # while also returning the value of the expression.
    # Ref: https://docs.python.org/3/reference/expressions.html#assignment-expressions
    while (cube := number ** 3) <= end:
        yield cube

        number += 1


gen = generate_cube_numbers(1)

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print('Ok')
