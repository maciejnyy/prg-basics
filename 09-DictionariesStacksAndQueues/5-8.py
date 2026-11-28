prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total_cost = sum(prices[item] * qty for item, qty in cart.items() if item in prices)
print(f"Total cost of the shopping cart: {total_cost:.2f}")
