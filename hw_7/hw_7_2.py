def correct_sentence(text: str) -> str:
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
