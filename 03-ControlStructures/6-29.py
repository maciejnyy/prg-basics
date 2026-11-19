n = int(input("Enter N: "))
primes = []
num = 2
while len(primes) < n:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        primes.append(num)
    num += 1
print("Prime numbers:", *primes)
