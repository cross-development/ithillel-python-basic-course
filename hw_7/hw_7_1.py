def say_hi(name: str, age: int) -> str:
    """
    Generates a greeting message introducing a person by their name and age.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.

    Returns:
        str: A greeting message in the format
             "Hi. My name is {name} and I'm {age} years old".

    Example:
        >>> say_hi("Alex", 32)
        "Hi. My name is Alex, and I'm 32 years old"
        >>> say_hi("Frank", 68)
        "Hi. My name is Frank, and I'm 68 years old"
    """

    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'

print('ОК')
