###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland.
# Test: 38, 27, 26, 22, 18
#
age = int(input('Enter age: '))
no_tax = age <= 26
print(f'Exemption from paying taxes: {no_tax}')
