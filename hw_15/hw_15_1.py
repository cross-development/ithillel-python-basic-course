from math import sqrt


class Rectangle:
    """
    A class representing a rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize the rectangle with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def get_square(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def __eq__(self, other: "Rectangle") -> bool:
        """
        Compare two rectangles by their area.

        Args:
            other (Rectangle): The other rectangle to compare with.

        Returns:
            bool: True if the areas are equal, otherwise False.
        """
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.get_square() == other.get_square()

    def __add__(self, other: "Rectangle") -> "Rectangle":
        """
       Add two rectangles by their area to create a new rectangle.

       Args:
           other (Rectangle): The other rectangle to add.

       Returns:
           Rectangle: A new rectangle with the combined area.
       """
        if not isinstance(other, Rectangle):
            return NotImplemented

        new_square = self.get_square() + other.get_square()
        new_width = sqrt(new_square)
        new_height = new_square / new_width

        return Rectangle(new_width, new_height)

    def __mul__(self, n: float) -> "Rectangle":
        """
        Multiply the rectangle's area by a number to create a new rectangle.

        Args:
            n (float): The multiplier.

        Returns:
            Rectangle: A new rectangle with the scaled area.
        """
        if not isinstance(n, (int, float)):
            return NotImplemented

        new_square = self.get_square() * n
        ratio = self.width / self.height
        new_width = sqrt(new_square * ratio)
        new_height = new_square / new_width

        return Rectangle(new_width, new_height)

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string describing the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print('OK')
