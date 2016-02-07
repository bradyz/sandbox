MAX_N = 1000
prime = [True for _ in range(MAX_N)]
prime[0] = prime[1] = False
for i in range(2, MAX_N):
    if not prime[i]:
        continue
    for j in range(i + i, MAX_N, i):
        prime[j] = False
for x in range(MAX_N):
    if prime[x]:
        print(x)
