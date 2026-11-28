import queue

def rpn_calculator():
    stack = queue.LifoQueue()
    print("Enter RPN tokens one by one (number, +, -, *, /, or = to finish):")
    
    while True:
        token = input("> ").strip()
        if token == '=':
            if not stack.empty():
                print("Result:", stack.get())
            else:
                print("Stack is empty.")
            break
        elif token in ('+', '-', '*', '/'):
            b = stack.get()
            a = stack.get()
            if token == '+':
                stack.put(a + b)
            elif token == '-':
                stack.put(a - b)
            elif token == '*':
                stack.put(a * b)
            elif token == '/':
                stack.put(a / b)
        else:
            try:
                stack.put(float(token))
            except ValueError:
                print("Invalid input. Enter a number, operator, or '='.")

if __name__ == "__main__":
    rpn_calculator()
