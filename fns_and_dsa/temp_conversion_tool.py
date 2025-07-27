CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_FREEZING_POINT = 0
FAHRENHEIT_FREEZING_POINT = 32

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

if __name__ == "__main__":
    temp_c = 25
    temp_f = 77

    print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")
    print(f"{temp_f}°F = {fahrenheit_to_celsius(temp_f)}°C")
