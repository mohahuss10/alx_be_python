# temp_conversion_tool.py

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
