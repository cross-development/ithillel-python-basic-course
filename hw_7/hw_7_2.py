def correct_sentence(text: str) -> str:
    """
    Corrects a given sentence by ensuring it starts with a capital letter
    and ends with a period.

    If the first character of the input text is not capitalized, it will be converted
    to uppercase. If the input text does not end with a period, a period will be added
    at the end. Existing capitalization and punctuation are preserved if already correct.

    Args:
        text (str): The input sentence to be corrected.

    Returns:
        str: The corrected sentence starting with an uppercase letter and ending with a period.

    Examples:
        >>> correct_sentence("greetings, friends")
        'Greetings, friends.'
        >>> correct_sentence("hello")
        'Hello.'
        >>> correct_sentence("Greetings. Friends")
        'Greetings. Friends.'
        >>> correct_sentence("Greetings, friends.")
        'Greetings, friends.'
        >>> correct_sentence("greetings, friends.")
        'Greetings, friends.'
    """

    # Make the first letter capitalized
    text = text[0].upper() + text[1:]

    # Add a period at the end if it is not there
    if not text.endswith('.'):
        text += '.'

    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
