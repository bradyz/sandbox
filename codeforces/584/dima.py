n = int(input())
prime = [True for _ in range(n+1)]
primes = list()
prime[0] = False
prime[1] = False
ret = None
for i in range(n+1):
    if not prime[i]:
        continue
    primes.append(i)
    if n == i:
        ret = [i]
    for j in range(i+i, n+1, i):
        prime[j] = False
if not ret:
    second = dict()
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            if primes[i] + primes[j] == n:
                ret = [primes[i], primes[j]]
            second[primes[i] + primes[j]] = (primes[i], primes[j])
    if not ret:
        for x in primes:
            for y in second:
                if x + y == n:
                    ret = [x, second[y][0], second[y][1]]
print(len(ret))
print(" ".join(map(str, ret)))
