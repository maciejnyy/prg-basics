def f(n):
    if n == 1: return 0
    if n == 2: return 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b
if __name__ == "__main__":
    print(f(5))
    print(f(9))
