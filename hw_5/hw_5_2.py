while True:
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
            continue  # Ask for new input without exiting
        result = num1 / num2
    else:
        print("Invalid operator")
        continue  # Ask for new input without exiting

    # Output the result of the operation
    print(f"Result: {result}")

    # Asking if the user wants to continue
    continue_calculation = input(
        "Do you want to perform another calculation? (yes/y to continue, anything else to quit): ").lower()

    if continue_calculation not in ["yes", "y"]:
        print("Goodbye!")
        break  # Exit the loop and end the program
