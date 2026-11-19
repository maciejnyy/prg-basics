amount = int(input("Number of products purchased: "))
price = float(input("Product price: "))
if amount > 2:
    total = 2 * price + (amount - 2) * price * 0.75
else:
    total = amount * price
print(f"Amount to pay: {total:.2f}")
