def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Prompt the user to enter two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Prompt the user to select an operation
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter your choice (1/2/3/4): ")
    
    # Perform the selected operation and display the result
    if operation == '1':
        result = num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
    else:
        print("\nInvalid operation choice. Please select 1, 2, 3, or 4.")

# Run the calculator
calculator()
