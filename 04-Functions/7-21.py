def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)
if __name__ == "__main__":
    print(f(7, 4, 9))
    print(f(2, 12, 8))
