import string
import keyword

# Asking the user to enter a string
user_input = input("Enter a string to check if this string can be a variable name: ")

can_be_variable_name = True

# Checking if the string starts with a number
if user_input[0].isdigit():
    can_be_variable_name = False
# Checking for capital letters
elif any(char.isupper() for char in user_input):
    can_be_variable_name = False
# Checking if the input string contains spaces
elif " " in user_input:
    can_be_variable_name = False
# Checking if the input string contains punctuation, other than underscores
elif any(char in string.punctuation for char in user_input) and "_" not in user_input:
    can_be_variable_name = False
# Checking if the string is a reserved word
elif user_input in keyword.kwlist:
    can_be_variable_name = False
# Checking if there are underscores in the wrong places
elif "__" in user_input:
    can_be_variable_name = False

# Output the result
print(can_be_variable_name)
