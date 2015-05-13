from bisect import bisect_left as bl
from bisect import bisect_right as br

a = int(input())
c = [int(x) for x in input()]

for i in range(1, len(c)):
    c[i] += c[i-1]

res = 0

for i in range(len(c)):
    l = bl(c, c[i]+a, lo=i+1)
    r = br(c, c[i]+a)
    if c[i] == a:
        res += 1
    if l != r:
        res += r - l

print(res)
