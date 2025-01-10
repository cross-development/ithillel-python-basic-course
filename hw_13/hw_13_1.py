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
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"


class Student(Human):
    """
    A class representing a student, inheriting from Human.

    Attributes:
        All attributes from Human class, plus:
        record_book (str): The student's record book number
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:
    """
    A class representing a group of students.

    Attributes:
        number (str): The group's identifier
        group (set): A set of Student instances
    """

    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        """
        Add a student to the group.

        Args:
            student (Student): The student instance to add
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
            last_name (str): The last name to search for

        Returns:
            Student or None: The found student instance or None if not found
        """
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self) -> str:
        all_students = '\n'.join(str(student) for student in self.group)

        return f'Number:{self.number}\n{all_students}\n'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
