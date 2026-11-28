import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '([{':
            stack.put(char)
        elif char in ')]}':
            if stack.empty() or stack.get() != matching[char]:
                return False
    return stack.empty()

for i, expr in enumerate([expression1, expression2, expression3], 1):
    if brackets_ok(expr):
        print(f"Expression {i}: brackets are OK")
    else:
        print(f"Expression {i}: brackets are NOT correct")
