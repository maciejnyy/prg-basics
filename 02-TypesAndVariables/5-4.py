###
# Reads an amount and prints the amount and its 23% VAT.
#
amount = float(input('Enter amount: '))
vat = amount * 0.23
print(f'Amount  : {amount:5.2f}')
print(f'VAT 23% : {vat:5.2f}')
