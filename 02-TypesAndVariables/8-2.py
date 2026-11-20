###
# Calculation of circle area and circumference
# Test: r = 1 --> circumference = 6.28, area = 3.14
#       r = 3 --> circumference = 18.84, area = 28.26
#

# determine radius and PI values
r = float(input('Enter radius: '))
PI = 3.14
# calculate area
area = PI * r ** 2
# calculate circumference
circumference = 2 * PI * r
# print results
print(f'Circumference = {circumference:.2f}')
print(f'Area = {area:.2f}')
