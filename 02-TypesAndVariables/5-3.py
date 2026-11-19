###
# A program that calculates the volume
# and surface area of a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
# Test: a = 3, b = 4, c = 5 --> volume = 60, surface area = 94
#       a = 8, b = 1, c = 2 --> volume = 16, surface area = 52
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)
print(f'Volume = {volume}')
print(f'Surface area = {surface_area}')
