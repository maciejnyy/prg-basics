def f(amount_to_pay):
    c5 = amount_to_pay // 5
    amount_to_pay %= 5
    c2 = amount_to_pay // 2
    amount_to_pay %= 2
    return c5 + c2 + amount_to_pay
if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))
