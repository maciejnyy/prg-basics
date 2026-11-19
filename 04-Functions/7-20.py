def f(n):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
        num += 1
    return primes[-1]
if __name__ == "__main__":
    print(f(1))
    print(f(5))
