###
# A program that calculates
# how many letters are between two given letters
# Test: A and D (2), B and M (10), K and K (0)
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = max(0, last_letter_code - first_letter_code - 1)
print(f'Between {first} and {last} is {number_of_letters} letters')
