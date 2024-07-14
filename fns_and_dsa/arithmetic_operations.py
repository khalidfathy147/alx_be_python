def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the given parameters.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float: The result of the operation.
        str:  A message indicating division by zero.

    Raises:
        ValueError: If an invalid operation is provided.
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        raise ValueError(f"Invalid operation: {operation}")