# Asking the user to enter a number
num1 = int(input("Enter first number: "))

# Asking the user to enter a number
num2 = int(input("Enter second number: "))

# Asking the user to enter a math operator (+, -, *, /)
operator = input("Enter operator (+, -, *, /): ")

# Calculating the result depending on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Checking if the value is not equal to zero
    if num2 == 0:
        print("You cannot divide by zero")
        exit()  # Terminate the app
    result = num1 / num2
else:
    print("Invalid operator")
    exit()  # Terminate the app

# Output the result of the operation
print(f"Result: {result}")
