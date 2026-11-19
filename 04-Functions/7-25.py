def f(x, y):
    return sum(i for i in range(x, y + 1) if i % 6 == 0 and i % 4 != 0)
if __name__ == "__main__":
    print(f(1, 20))
    print(f(10, 30))
