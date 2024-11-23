# Asking the user to enter a 4-digit number
user_number = int(input("Enter a 4-digit number: "))

# Use divmod to split a number into digits
digit1, remainder = divmod(user_number, 1000)  # Get the first digit and the remainder
digit2, remainder = divmod(remainder, 100)  # Get the second digit and the remainder
digit3, digit4 = divmod(remainder, 10)  # Get the third and fourth digits

# Print the digits in a column
print(digit1)
print(digit2)
print(digit3)
print(digit4)
