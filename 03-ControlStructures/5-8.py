balance = 1000
pin = '1111'
while True:
    print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Check PIN\n5. Change PIN\n0. Exit")
    choice = input("Choose: ")
    if choice == '0': break
    elif choice == '1': print(f"Balance: {balance}")
    elif choice == '2': balance += float(input("Amount: "))
    elif choice == '3': balance -= float(input("Amount: "))
    elif choice == '4': print("PIN is correct" if input("Enter PIN: ") == pin else "Invalid PIN")
    elif choice == '5': 
        new_pin = input("Enter new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4: 
            pin = new_pin
            print("PIN changed")
        else: 
            print("Invalid format")
