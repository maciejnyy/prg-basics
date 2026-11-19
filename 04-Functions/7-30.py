def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)
if __name__ == "__main__":
    print(sum_natural(10))
