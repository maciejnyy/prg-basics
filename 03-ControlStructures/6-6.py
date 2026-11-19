hours = int(input("Parking hours: "))
if hours <= 2: fee = 5
elif hours <= 6: fee = 15
else: fee = 20
print(f"Fee: {fee} PLN")
