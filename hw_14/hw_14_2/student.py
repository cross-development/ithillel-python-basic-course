from human import Human


class Student(Human):
    """
    A class representing a student, inheriting from Human.

    Attributes:
        All attributes from Human class, plus:
        record_book (str): The student's record book number
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        """
        Initialize a Student instance.

        Args:
            gender (str): The student's gender.
            age (int): The student's age.
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            record_book (str): The student's record book number.
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Return a string representation of the Student instance.

        Returns:
            str: A formatted string with student information.
        """
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other: object) -> bool:
        """
        Compare two Student instances based on their string representation.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, Student):
            return False

        return str(self) == str(other)

    def __hash__(self) -> int:
        """
        Make the Student instance hashable by using its string representation.

        Returns:
            int: The hash value of the student.
        """
        return hash(str(self))
