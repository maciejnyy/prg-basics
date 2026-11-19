def f(x, y):
    return sum(1 for i in range(x, y + 1) if i < 0 and i % 2 == 0)
if __name__ == "__main__":
    print(f(-7, 8))
    print(f(-1, 11))
