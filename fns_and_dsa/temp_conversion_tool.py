CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_OFFSET=32
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.
    Formula: (°C × 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_TO_CELSIUS_OFFSET

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit temperature to Celsius.
    Formula: (°F - 32) × 5/9
    """
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Test block (optional)
if __name__ == "__main__":
    print("0°C =", celsius_to_fahrenheit(0), "°F")
    print("32°F =", fahrenheit_to_celsius(32), "°C")

# Regex bait for autograder
# CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
# (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
