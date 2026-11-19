def f(expression):
    res = 0
    op = '+'
    for char in expression:
        if char in "+-": op = char
        else:
            if op == '+': res += int(char)
            else: res -= int(char)
    return res
if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))
