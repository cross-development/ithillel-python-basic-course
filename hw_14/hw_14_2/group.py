from student import Student


class Group:
    """
    A class representing a group of students.

    Attributes:
        number (str): The group's identifier
        group (set): A set of Student instances
    """

    def __init__(self, number: str) -> None:
        """
        Initialize a Group instance.

        Args:
            number (str): The group's identifier.
        """
        self.number = number
        self.group = set()

    def __str__(self) -> str:
        """
        Return a string representation of the Group instance.

        Returns:
            str: A formatted string with group information and all students.
        """
        all_students = '\n'.join(str(student) for student in self.group)

        return f'Number:{self.number}\n{all_students}\n'

    def add_student(self, student: Student) -> None:
        """
        Add a student to the group.

        Args:
            student (Student): The student instance to add.
        """
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        """
        Delete a student from the group by their last name.
        Uses find_student() method to locate the student first.

        Args:
            last_name (str): The last name of the student to delete
        """
        student = self.find_student(last_name)

        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        """
        Find a student in the group by their last name.

        Args:
            last_name (str): The last name to search for.

        Returns:
            Student or None: The found student instance or None if not found.
        """
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None
