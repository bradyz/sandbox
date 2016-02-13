N = 1000001
vis = set()
prime = [True for _ in range(N)]
prime[0] = prime[1] = False
primes = {i: set() for i in range(1, len(str(N)))}
for i in range(2, N):
    if not prime[i]:
        continue
    primes[len(str(i))].add(str(i))
    for j in range(i+i, N, i):
        prime[j] = False
ret = 0
for l in primes:
    for val in sorted(primes[l]):
        if val in vis:
            continue
        vis.add(val)
        tmp = val
        rotated = [tmp]
        for i in range(len(val)-1):
            tmp = tmp[-1] + tmp[:-1]
            vis.add(tmp)
            if tmp not in primes[l]:
                break
            rotated.append(tmp)
        if len(rotated) == len(val):
            ret += len(set(rotated))
print(ret)
