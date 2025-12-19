import queue

def toBinary(number):
    stack = queue.LifoQueue()
    binary_number = ""
    while number != 0:
        rest = number % 2
        stack.put(rest)
        number = number // 2
    while not stack.empty():
        binary_number += str(stack.get())
    return binary_number

print(toBinary(1023))

