def safe_divide(numerator, denominator):
  """Performs division with error handling for ZeroDivisionError and non-numeric inputs.

  Args:
    numerator: The number to be divided.
    denominator: The number to divide by.

  Returns:
    The result of the division if successful, otherwise an error message.
  """
  try:
    numerator = float(numerator)
    denominator = float(denominator)
    if denominator == 0:
      return "Error: Cannot divide by zero."
    else:
      return numerator / denominator
  except ValueError:
    return "Error: Please enter numeric values only."
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."