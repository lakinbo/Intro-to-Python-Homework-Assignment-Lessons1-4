# Create a calculator using functions for different operations.

# Requirements:

    # Create these functions:
        # add(a, b) - returns the sum of two numbers
        # subtract(a, b) - returns the difference of two numbers
        # multiply(a, b) - returns the product of two numbers
        # divide(a, b) - returns the quotient, handles division by zero
    # Create a main function that:
        # Gets two numbers from the user
        # Asks which operation to perform
        # Calls the appropriate function
        # Displays the result

def add(a, b):
    result = a + b
    return f"{a} + {b} = {result}"

def subtract (a, b):
    result = a - b
    return f"{a} - {b} = {result}"

def multiply(a, b):
    result = a * b
    return f"{a} * {b} = {result}"

def divide (a, b):
    if b == 0:
        return ("Error: Cannot divide by zero!")
    else:
        result = a / b
        return f"{a} ÷ {b} = {result}"

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

        operation = int(input("Enter choice (1 - 4): "))
        if operation == 1:
            print(add(num1, num2))
        elif operation == 2:
            print(subtract(num1, num2))
        elif operation == 3:
            print(multiply(num1, num2))
        elif operation == 4:
            print(divide(num1, num2))
        else:
            print("Invalid input!")
    except ValueError:
        print("Invalid input!")


main()

