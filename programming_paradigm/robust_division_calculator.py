def safe_divide(numerator, denominator):
    """
    Performs division with comprehensive error handling
    Args:
        numerator: number to be divided
        denominator: number to divide by
    Returns:
        str: formatted result or error message
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."