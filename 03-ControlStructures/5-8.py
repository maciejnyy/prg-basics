balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print() 
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("Incorrect PIN.")
    elif choice == '5':
        new_pin = input("Enter new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            pin = new_pin
            print("PIN successfully changed.")
        else:
            print("Invalid PIN format. It must be exactly 4 digits.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break
    else:
        print("Invalid option. Please try again.")
