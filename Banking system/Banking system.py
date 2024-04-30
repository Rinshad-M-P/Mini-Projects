def add(num1, num2):
    """Performs addition on two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Performs subtraction on two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Performs multiplication on two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Performs division on two numbers, handling division by zero."""
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

def num_input(prompt):
    """Gets a valid number input from the user."""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation():
    """Gets a valid operation input from the user."""
    while True:

        operation = input("Select operation: \n+ \n* \n- \n/ \nEnter your choice: ")

        if operation in ("+", "-", "*", "/"):
            return operation
        else:
            print("Invalid input. Please enter a valid choice.")


def calculator():
    """Main function that runs the calculator loop."""

    num1 = num_input("Enter first number: ")

    while True:
        operation = get_operation()
        num2 = num_input("Enter second number: ")

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print("\nResult:", result)

        choice = input(
            f"\nEnter 'y' to continue this operation with {result}. \nEnter 'n' to start new calculation. \nEnter any "
            f"key except 'y' or 'n' for exit. \n\nEnter your choice: ").lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            calculator()
            break
        else:
            print("\nClaculator closed.")
            break

calculator()
