# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR - 32

def convert_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# User interaction
temperature = input("Enter the temperature to convert: ")
try:
  temperature = float(temperature)
  unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

  if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
  elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
  else:
    print("Invalid unit. Please enter C or F.")
except ValueError:
  print("Invalid temperature. Please enter a numeric value.")