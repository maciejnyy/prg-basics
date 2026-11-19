###
# Price before and after discount.
#
price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
price_with_discount = price * (1 - discount / 100)
reduction = price - price_with_discount
print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduction: {reduction:.2f}')
