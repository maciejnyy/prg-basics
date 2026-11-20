import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown > 5:
        print(countdown)
    elif countdown == 5:
        print("five")
    elif countdown == 4:
        print("four")
    elif countdown == 3:
        print("three")
    elif countdown == 2:
        print("two")
    elif countdown == 1:
        print("one")
    
    countdown -= 1
    time.sleep(1)

print("Time's up!")
