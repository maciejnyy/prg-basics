def f(n1, n2, n3):
    return any(n < 0 for n in (n1, n2, n3))
if __name__ == "__main__":
    print(f(11, 6, -4))
    print(f(5, 4, 14))
