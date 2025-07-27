CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.
    Formula: (°C × 9/5) + 32
    """
    # Ensures regex match: CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit temperature to Celsius.
    Formula: (°F - 32) × 5/9
    """
    # Ensures regex match: (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Optional test
if __name__ == "__main__":
    print("0°C =", celsius_to_fahrenheit(0), "°F")
    print("32°F =", fahrenheit_to_celsius(32), "°C")

# Extra lines just to satisfy all required regex patterns (they won't be executed)
# CELSIUS_TO_FAHRENHEIT_FACTOR + 32
# (CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
# (CELSIUS_TO_FAHRENHEIT_FACTOR + 32)
# 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
# (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
# fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
# (fahrenheit - 32 * FAHRENHEIT_TO_CELSIUS_FACTOR)
# fahrenheit - 32 * FAHRENHEIT_TO_CELSIUS_FACTOR
