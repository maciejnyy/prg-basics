###
# A program that checks whether the number entered
# from the keyboard is even.
# Test: 24, 8, 31, 5
#
number = int(input('Enter number: '))
even = number % 2 == 0
print(f'Number is even: {even}')
