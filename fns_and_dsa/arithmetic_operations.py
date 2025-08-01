def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        num1: First number
        num2: Second number
        operation: One of 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        Result of the arithmetic operation or error message string
    """
    operation = operation.strip().lower()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
