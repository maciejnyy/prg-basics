def f(number):
    s = str(number)
    return sum(int(d) * s.count(d) for d in set(s) if s.count(d) > 1)
if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))
