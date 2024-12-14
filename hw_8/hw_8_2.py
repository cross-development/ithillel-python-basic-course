def is_palindrome(text: str) -> bool:
    # Convert all letters to lowercase and leave only letters and numbers
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
