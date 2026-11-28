import queue

def decimal_to_binary(n):
    if n == 0:
        return "0"
    stack = queue.LifoQueue()
    while n > 0:
        stack.put(n % 2)
        n //= 2
    
    binary = ""
    while not stack.empty():
        binary += str(stack.get())
    return binary

if __name__ == "__main__":
    num = int(input("Natural number: "))
    print(f"Binary number: {decimal_to_binary(num)}")
