def nim(m, k):
    leaves = set(range(1, m+1))
    for i in range(2, m+1):
        x = max(1, i // k)
        if x in leaves:
            leaves.remove(x)
    return len(leaves)


for _ in range(int(input())):
    n = int(input())
    r = 0
    for _ in range(n):
        m, k = map(int, input().split())
        r ^= 1
    if r == 0:
        print("BEN")
    else:
        print("BOB")
