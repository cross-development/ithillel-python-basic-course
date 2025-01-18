from math import gcd


class Fraction:
    """
    Represents a mathematical fraction with a numerator and a denominator.
    Provides methods for arithmetic operations, comparisons, and simplification.

    Attributes:
        a (int): The numerator of the fraction.
        b (int): The denominator of the fraction.
    """

    def __init__(self, a: int, b: int) -> None:
        """
        Initializes a Fraction instance.

        Args:
            a (int): The numerator of the fraction.
            b (int): The denominator of the fraction.

        Raises:
            ValueError: If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    def simplify(self) -> 'Fraction':
        """
        Simplifies the fraction by dividing the numerator and denominator
        by their greatest common divisor (GCD).

        Returns:
            Fraction: A new simplified Fraction instance.
        """
        common_divisor = gcd(self.a, self.b)

        return Fraction(self.a // common_divisor, self.b // common_divisor)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Multiplies this fraction by another fraction.

        Args:
            other (Fraction): The other fraction to multiply by.

        Returns:
            Fraction: A new Fraction instance representing the product.
        """
        new_a = self.a * other.a
        new_b = self.b * other.b

        return Fraction(new_a, new_b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Adds this fraction to another fraction.

        Args:
            other (Fraction): The other fraction to add.

        Returns:
            Fraction: A new Fraction instance representing the sum.
        """
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b

        return Fraction(new_a, new_b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Subtracts another fraction from this fraction.

        Args:
            other (Fraction): The other fraction to subtract.

        Returns:
            Fraction: A new Fraction instance representing the difference.
        """
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b

        return Fraction(new_a, new_b)

    def __eq__(self, other: 'Fraction') -> bool:
        """
        Checks if two fractions are equal after simplification.

        Args:
            other (Fraction): The other fraction to compare.

        Returns:
            bool: True if the fractions are equal, False otherwise.
        """
        simplified_self = self.simplify()
        simplified_other = other.simplify()
        are_fractions_equal = (simplified_self.a == simplified_other.a and
                               simplified_self.b == simplified_other.b)

        return are_fractions_equal

    def __gt__(self, other: 'Fraction') -> bool:
        """
        Checks if this fraction is greater than another fraction.

        Args:
            other (Fraction): The other fraction to compare.

        Returns:
            bool: True if this fraction is greater, False otherwise.
        """
        return self.a * other.b > self.b * other.a

    def __lt__(self, other: 'Fraction') -> bool:
        """
        Checks if this fraction is less than another fraction.

        Args:
            other (Fraction): The other fraction to compare.

        Returns:
            bool: True if this fraction is less, False otherwise.
        """
        return self.a * other.b < self.b * other.a

    def __str__(self) -> str:
        """
        Returns a string representation of the fraction.

        Returns:
            str: The string representation of the fraction.
        """
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
