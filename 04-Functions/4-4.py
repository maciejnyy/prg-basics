###
# Calculates the sum of the digits in a number
#
import math
def sum_digits(number):
    if number < 0:
        number = abs(number)
    number = str(number)
    digits_sum = 0
    for i in number:
        digit = int(i)
        digits_sum += digit
    return digits_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')