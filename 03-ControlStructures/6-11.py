current = float(input("Current product price: "))
previous = float(input("Previous product price: "))
decrease = (previous - current) / previous * 100
if decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(decrease)}%")
