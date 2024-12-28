from inspect import isgenerator
from typing import Generator


def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Generate prime numbers up to a given upper limit.

    Args:
        end: The upper limit (inclusive) for generating prime numbers.

    Yields:
        The next prime number in the range from 2 to `end`.
    """

    def is_prime(number: int) -> bool:
        """Check if a number is a prime."""
        if number < 2:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False

        return True

    # Generator expression to filter prime numbers in range
    # Ref: https://docs.python.org/3/reference/expressions.html#yield-expressions
    yield from (n for n in range(2, end + 1) if is_prime(n))


gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')
