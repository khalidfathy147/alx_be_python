# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius."""
  return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit."""
  return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

def main():
  """Prompts the user for temperature and unit, performs conversion, and displays the result."""
  try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit == 'C':
      converted_temperature = convert_to_fahrenheit(temperature)
      print(f"{temperature}°C is {converted_temperature}°F")
    elif unit == 'F':
      converted_temperature = convert_to_celsius(temperature)
      print(f"{temperature}°F is {converted_temperature}°C")
    else:
      raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
  

if __name__ == "__main__":
  main()