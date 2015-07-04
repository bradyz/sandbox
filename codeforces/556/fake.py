n = int(input())
c = list(map(int, input().split()))
u = set()
r = True

while len(u) < n:
    u.add(c[0])
    for i in range(n):
        if i % 2 == 0:
            c[i] = (c[i] + 1) % n
        else:
            c[i] = (c[i] - 1) % n
    r = True
    for i in range(n):
        if c[i] != i:
            r = False
            break
    if r:
        break

if r:
    print("Yes")
else:
    print("No")
