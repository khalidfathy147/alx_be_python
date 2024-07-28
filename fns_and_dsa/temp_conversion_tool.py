# Define global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
# User interaction
temp = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

# Handle user input
if unit == "F":
    result = convert_to_celsius(temp)
else:
    result = convert_to_fahrenheit(temp)

# Display result
print(f"{temp}°{unit} is {result:.2f}°C")

# Error handling
try:
    float(temp)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
