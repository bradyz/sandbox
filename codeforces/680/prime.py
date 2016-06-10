prime = [True for _ in range(101)]
prime[0] = False
prime[1] = False
for i in range(2, 101):
    if not prime[i]:
        continue
    for j in range(i + i, 101, i):
        prime[j] = False
y = list(x for x in range(101) if prime[x] and x <= 50)
c = 0
for v in y + [4, 9, 25, 49]:
    print(v)
    c += (input() == "yes")
if c < 2:
    print("prime")
else:
    print("composite")
