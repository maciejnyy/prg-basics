pin = "0805"
attempts = 0
while attempts < 3:
    p = input("Enter the PIN code: ")
    if p == pin:
        print("Correct")
        break
    else:
        print("Incorrect...")
        attempts += 1
if attempts == 3:
    print("Sorry, your payment card has been blocked.")
