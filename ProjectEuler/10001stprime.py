n = 2
while True:
    prime = [True for _ in range(n)]
    prime[0] = False
    prime[1] = False
    primes = list()
    for i in range(2, n):
        if not prime[i]:
            continue
        for j in range(i + i, n, i):
            prime[j] = False
        primes.append(i)

    if len(primes) < 10001:
        n *= 2
    else:
        print(primes[10000])
        break
