# 474B: Worms
# Start Time: 4:32 p.m. 5-1-15
# End Time: 4:54 a.m. 5-1-15 runtime error dunno why

from bisect import bisect_left as bl

if __name__ == "__main__":
    v = [0 for _ in range(10**5 + 1)]
    n = int(input())
    c = list(map(int, input().split()))

    for i in range(1, n):
        c[i] += c[i-1]

    s = 0
    for idx, val in enumerate(c):
        for _ in range(val):
            v[s] = idx + 1
            s += 1

    q = int(input())
    t = list(map(int, input().split()))

    for val in t:
        print(bl(c, val-1) + 1)
