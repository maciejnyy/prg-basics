import queue

customer_queue = queue.Queue()
ticket_number = 1

while True:
    print("\n1. New customer (issue ticket)")
    print("2. Serve next customer")
    print("0. Exit")
    choice = input("Select an option: ")
    
    if choice == '1':
        customer_queue.put(ticket_number)
        print(f"Ticket #{ticket_number} issued and added to the queue.")
        ticket_number += 1
    elif choice == '2':
        if not customer_queue.empty():
            served = customer_queue.get()
            print(f"Now serving customer with ticket #{served}.")
        else:
            print("No customers in the queue.")
    elif choice == '0':
        break
    else:
        print("Invalid option.")
