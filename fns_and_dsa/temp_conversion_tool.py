# Global conversion factors - MUST BE DEFINED EXACTLY LIKE THIS
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    return fahrenheit

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temp = float(temp_input)
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
        
        if unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()