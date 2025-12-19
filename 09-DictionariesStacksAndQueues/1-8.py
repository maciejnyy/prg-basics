
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print('Before the discount:')
value = 0
for product,cost in price_list.items():
    print(f'{product}: {cost}')
    value += cost
value_round = round(value,2)
print(f'Total value before discount: {value_round}')
value2 = 0
print('After the discount:')
for product,cost in price_list.items():
    cost = round(cost*0.9,2)
    print(f'{product}: {cost}')
    value2 += cost
print(f'Total value after discount: {round(value2,2)}')