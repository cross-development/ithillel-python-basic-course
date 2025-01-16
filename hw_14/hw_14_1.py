class GroupLimitError(Exception):
    """
    Custom exception raised when adding more than 10 students to a group.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class Human:
    """
    A class representing a human with basic personal information.

    Attributes:
        gender (str): The person's gender
        age (int): The person's age
        first_name (str): The person's first name
        last_name (str): The person's last name
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        """
        Initialize a Human instance.

        Args:
            gender (str): The person's gender.
            age (int): The person's age.
            first_name (str): The person's first name.
            last_name (str): The person's last name.
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Return a string representation of the Human instance.

        Returns:
            str: A formatted string with personal information.
        """
        return f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"


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
            student (Student): The student instance to add

        Raises:
            GroupLimitError: If the group already contains 10 students.
        """
        if len(self.group) >= 10:
            raise GroupLimitError("Group cannot contain more than 10 students")

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
            last_name (str): The last name to search for

        Returns:
            Student or None: The found student instance or None if not found
        """
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
st4 = Student('Female', 23, 'Alice', 'Smith', 'AN147')
st5 = Student('Male', 24, 'Bob', 'Brown', 'AN148')
st6 = Student('Female', 26, 'Cindy', 'White', 'AN149')
st7 = Student('Male', 27, 'Dan', 'Green', 'AN150')
st8 = Student('Female', 28, 'Emma', 'Black', 'AN151')
st9 = Student('Male', 29, 'Frank', 'Blue', 'AN152')
st10 = Student('Female', 20, 'Grace', 'Yellow', 'AN153')
st11 = Student('Male', 21, 'Harry', 'Red', 'AN154')

gr = Group('PD1')

try:
    students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]

    for student in students:
        gr.add_student(student)

    print(gr)

    # Attempt to add the 11th student (should raise exception)
    gr.add_student(st11)
except GroupLimitError as e:
    print(f"Error: {e}")

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')  # No error!
