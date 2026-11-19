def f(product_code):
    s = sum(int(product_code[i]) for i in range(3))
    return s % 7 == int(product_code[3])
if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
