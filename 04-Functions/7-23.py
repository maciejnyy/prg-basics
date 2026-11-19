def f(password):
    return len(password) >= 6 and len(password) == len(set(password))
if __name__ == "__main__":
    print(f("ax15"))
    print(f("A2water3"))
