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
