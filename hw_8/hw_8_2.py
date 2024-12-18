def is_palindrome(text: str) -> bool:
    """
    Check if the given text is a palindrome, ignoring non-alphanumeric characters and case.

    A palindrome is a word, phrase, number, or other sequence of characters that reads the same
    forward and backward, ignoring spaces, punctuation, and letter casing.

    Args:
        text (str): The string to check for palindrome properties.

    Returns:
        bool: True if the text is a palindrome, False otherwise.

    Example:
        >>> is_palindrome('A man, a plan, a canal: Panama')
        True
        >>> is_palindrome('0P')
        False
    """

    # Convert all letters to lowercase and leave only letters and numbers
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
