# Asking the user to enter a 5-digit number
user_number = int(input("Enter a 5-digit number: "))

# Highlight the digits of the number using divmod
digit1, remainder = divmod(user_number, 10000)
digit2, remainder = divmod(remainder, 1000)
digit3, remainder = divmod(remainder, 100)
digit4, digit5 = divmod(remainder, 10)

# Solution 1: collect the inverted number
reversed_number = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1

# Solution 2: convert a number to a string, flip it over and back to an integer
# reversed_number = int(str(number)[::-1])

# Print the result
print(reversed_number)
