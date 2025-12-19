import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        # opening brackets → push to stack
        if char in '([{':
            stack.put(char)

        # closing brackets → pop and compare
        elif char in ')]}':
            if stack.empty():
                return False

            top = stack.get()
            if brackets[char] != top:
                return False

    # stack must be empty at the end
    return stack.empty()

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct

if brackets_ok(expression1):
    print("Expression 1: brackets are OK")
else:
    print("Expression 1: brackets are NOT correct")

if brackets_ok(expression2):
    print("Expression 2: brackets are OK")
else:
    print("Expression 2: brackets are NOT correct")

if brackets_ok(expression3):
    print("Expression 3: brackets are OK")
else:
    print("Expression 3: brackets are NOT correct")
