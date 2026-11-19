def f(number, even):
    s = 0
    for digit in str(number):
        d = int(digit)
        if even and d % 2 == 0: s += d
        elif not even and d % 2 != 0: s += d
    return s
if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
