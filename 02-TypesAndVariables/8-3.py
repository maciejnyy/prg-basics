###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# read the temperature in Celsius from the keyboard
celsius = float(input('Enter temperature in Celsius: '))
# calculate Kelvin: K = C + 273.15
kelvin = celsius + 273.15
# calculate Fahrenheit: F = C * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32
# print results
print(f'Temperature in Kelvin: {kelvin:.2f}')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f}')
