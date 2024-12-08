# Get a number from the user
user_number = int(input("Enter an integer: "))

# The loop is executed while the number is greater than 9
while user_number > 9:
    product = 1

    # Convert the number to a string and multiply all its digits
    for digit in str(user_number):
        product *= int(digit)

    # Update the number
    user_number = product

# Output the result
print(user_number)
