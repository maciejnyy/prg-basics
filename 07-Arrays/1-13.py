# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

lenght = len(product_prices)
i = 0
value_all = 0
value_summary = 0

while i < lenght:
    value_summary = product_prices[i] * product_quantities[i]
    value_all += value_summary
    i += 1

print(value_all)