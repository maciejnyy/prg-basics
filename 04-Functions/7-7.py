def f(binary_number):
    return all(c in '01' for c in str(binary_number))
if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))
